"""
    Manage database changes, like upload and delete.
    It is specifically designed with Django ORM syntax.

    Classes:
        UploadQueries

        DeleteQueries

    Exceptions:
        NIL

    Functions:
        NIL
"""

from food_items.models import Product, Store, Category
from datetime import datetime, timezone


class UploadQueries():
    def query_upload_stores(self, store_list):
        store_list = [Store(name=store) for store in store_list]
        Store.objects.bulk_create(store_list)

    def query_upload_categories(self, category_list):
        category_list = [Category(name=category) for category in category_list]
        Category.objects.bulk_create(category_list)

    def _add_products_to_db(self, product_list):
        products_to_upload = [(Product(code=item[2], brand=item[0],
                               name=item[1],
                               last_modified=datetime.fromtimestamp(
                                   int(item[7]), timezone.utc),
                               nutrition_score=item[3],
                               image_url=item[6])) for item in product_list]
        Product.objects.bulk_create(products_to_upload)

    def _add_stores_categories_to_product(self, product_list):
        """
            As stores and categories are linked to products through
            join tables, their relation is established here.

            Arguments:
                product_list: to be noticed, Stores and Categories
                have already been converted into a list.

            Returns:
                None.
        """
        for item in product_list:
            store_list = list()
            product = Product.objects.get(code=item[2])
            for store in item[4]:
                try:
                    store_list.append(Store.objects.get(name=store))
                except Exception:
                    pass
            category_list = []
            for category in item[5]:
                try:
                    category_list.append(Category.objects.get(name=category))
                except Exception:
                    pass
            product.stores.set(store_list)
            product.categories.set(category_list)
            product.save()

    def query_upload_products(self, product_list):
        self._add_products_to_db(product_list)
        self._add_stores_categories_to_product(product_list)

    def query_count_products(self):
        return Product.objects.count()


class DeleteQueries:

    def query_delete_all_categories(self):
        Category.objects.all().delete()

    def query_delete_all_stores(self):
        Store.objects.all().delete()

    def query_delete_all_products(self):
        Product.objects.all().delete()
