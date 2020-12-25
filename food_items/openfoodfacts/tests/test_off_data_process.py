"""
    This module tests the step-by-step processing of the data from the download
    from Open Food Facts to the upload in the database.
    Tests are arranged in accordance with the type of data:
    Stores, Categories, Products.

    Classes:
        TestConnectionOFF: tests the effective connection with Open Food Facts:
        we should get a 200 OK response type. No data is downloaded.

        TestProcessStore: organized in two steps : effective data download and
        processing of a mock dataset for test purposes.

        TestProcessCategory: built on the same principles than the stores

        TestUploadProduct: checks that a product is correctly processed to
        be added to the DB, including its relation to the join tables.

        TestProcessProduct: test the full process of a product:
        - construction of the download request,
        - data processing,
        - upload in a test DB.

    Exceptions:
        NIL

    Functions:
        NIL
"""

import requests
from django.test import TestCase
from food_items.tests import fixture as f
from food_items.models import Product, Store, Category
from food_items.openfoodfacts.off_data_process import ProcessStore,\
                                                      ProcessCategory,\
                                                      ProcessProduct
from food_items.openfoodfacts.config import OpenFoodFactsParams
from food_items.openfoodfacts.tests.mock_data import MockDataOFF, MockProducts
from food_items.openfoodfacts.queries import UploadQueries
from unittest.mock import Mock, patch


class TestConnectionOFF(TestCase, OpenFoodFactsParams):
    def test_connexion_OFF(self):
        r = requests.get(self.URL, headers=self.HEADERS)
        self.assertEqual(r.status_code, 200)


class TestProcessStore(TestCase, ProcessStore, OpenFoodFactsParams,
                       MockDataOFF):

    def test_download_stores(self):
        self.stores = self._download_stores()
        number_stores = self.stores.get('count')
        self.assertIsNotNone(self.stores)
        self.assertGreater(number_stores, 2000)

    @patch('requests.get')
    def test_store_full_process(self, mock_get):
        self.stores = self.from_data_to_list(self.store_data, "tags", "name")
        self._upload_stores(self.stores)
        self.assertGreater(Store.objects.count(), 200)


class TestProcessCategory(TestCase, ProcessCategory, OpenFoodFactsParams,
                          MockDataOFF):

    def test_download_categories(self):
        self.categories = self._download_categories()
        number_categories = self.categories.get('count')
        self.assertIsNotNone(self.categories)
        self.assertGreater(number_categories, 2000)

    @patch('requests.get', autospec=True)
    def test_category_full_process(self, mock_get):
        self.categories = self.from_data_to_list(self.category_data,
                                                 "tags", "name")
        self._upload_categories(self.categories)
        self.assertGreater(Category.objects.count(), 20)


class TestUploadProduct(TestCase, MockProducts, UploadQueries):
    def setUp(self):
        f.set_up_db()

    def test_query_upload_products(self):
        try:
            Product.objects.get(name="P'tit Nature Complet")
            self.fail("Le Produit est déjà en base !!")
        except Exception:
            self.query_upload_products(self.mock_product_list)
            product = Product.objects.get(name="P'tit Nature Complet")
            self.assertIsNotNone(product)
            self.assertEqual(len(
                            [store.name
                                for store in product.stores.all()]), 1)
            self.assertEqual(len(
                            [category.name
                                for category in product.categories.all()]), 5)


class TestProcessProduct(TestCase, ProcessProduct, OpenFoodFactsParams,
                         MockDataOFF):
    def setUp(self):
        f.set_up_db()

    def test_configure_request_payload(self):
        test_category, test_page_number = "Snacks", 1
        self.request_payload = self._configure_request_payload(
                                test_category, test_page_number)
        self.assertEqual(self.test_payload, self.request_payload)

    def _download_products(self):
        self.mock_response = Mock(return_value=self.product_data)
        return self.mock_response.return_value

    def test_sort_out_product_data(self):
        data_to_sort_out = self._download_products()
        self.data_sorted_out = self._sort_out_product_data(data_to_sort_out)
        self.assertEqual(len(self.data_sorted_out), 20)
        return self.data_sorted_out
