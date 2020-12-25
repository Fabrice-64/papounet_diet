"""
    This module contains the whole processing of Open Food Facts data,
    from the download to the upload in the database.
    They are closely linked w. the management/commands modules of this app.
    It is organized around the types of datat:
    - Stores,
    - Categories,
    - Products.

    Classes:
        ProcessStore

        ProcessCategory

        ProcessProduct

    Exceptions:
        NIL

    Functions:
        NIL
"""

import requests
import json
from food_items.openfoodfacts.shared_methods import DataCleaning
from food_items.openfoodfacts.config import OpenFoodFactsParams
from food_items.openfoodfacts.queries import UploadQueries, DeleteQueries


class ProcessStore(DataCleaning, OpenFoodFactsParams, UploadQueries):
    def _download_stores(self):
        response = requests.get(self.URL_STORES)
        return response.json()

    def _upload_stores(self, stores):
        self.query_upload_stores(stores)

    def store_full_process(self):
        self.stores = self._download_stores()
        # Here is room for optimization along category_full_process (DRY)
        self.stores = self.from_data_to_list(self.stores, "tags", "name")
        self._upload_stores(self.stores)


class ProcessCategory(DataCleaning, OpenFoodFactsParams, UploadQueries):
    def _download_categories(self):
        response = requests.get(self.URL_CATEGORIES)
        return response.json()

    def _upload_categories(self, categories):
        self.query_upload_categories(categories)

    def category_full_process(self):
        self.categories = self._download_categories()
        self.categories = self.from_data_to_list(self.categories,
                                                 "tags", "name")
        self._upload_categories(self.categories)


class ProcessProduct(DataCleaning, OpenFoodFactsParams, UploadQueries):
    def _configure_request_payload(self, category, page_number):
        # Product data in OFF DB are organized in pages, up to 1000 items.
        # Increment the page numbers allow larger downloads.
        self.payload.update({"tag_0": category})
        self.payload.update({"page": page_number})
        return self.payload

    def _download_products(self):
        r = requests.get(self.URL, headers=self.HEADERS, params=self.payload)
        self.product_data = r.json()
        return self.product_data

    def _sort_out_product_data(self, product_data):
        """
            The Open Food Facts database may look somehow messy.
            Therefore products have to be checked and cleaned before import.

            Arguments:
                product_data: is under a JSON format

            Returns:
                products_list: each product is organized as a tuple.
                All the products to be uploaded are organized into a list.
        """
        products_list = list()
        for product in product_data["products"]:
            # Need to discard the data where the nutrition grade is empty.
            if product.get('nutrition_grade_fr') is not None\
                            and product.get('stores') is not None:
                brand = product.get('brands')
                name = product.get('product_name')
                code = product.get('code')
                nutrition_score = product.get('nutrition_grade_fr')
                # Stores and categories are stores as strings in OFF.
                stores = self.from_string_into_list(product.get('stores'))
                categories = self.from_string_into_list(
                                    product.get('categories'))
                image_url = self.assign_url(product.get('image_url'))
                last_modified = product.get('last_modified_t')
                products_list.append((brand, name, code, nutrition_score,
                                      stores, categories, image_url,
                                      last_modified))
        return products_list

    def _product_full_process(self, category, page_number):
        self._configure_request_payload(category, page_number)
        product_data = self._download_products()
        product_list = self._sort_out_product_data(product_data)
        self.query_upload_products(product_list)

    def manage_full_set_products(self):
        # Room for optimization to choose other categories and more pages
        category = "Snacks"
        total_pages = 5
        for page in range(1, total_pages):
            self._product_full_process(category, page)
            print(f"Number of food items: {self.query_count_products()}")
