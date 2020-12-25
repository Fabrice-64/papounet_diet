"""
    Data from Open Food Facts need to be cleaned up before being inserted
    into the DB. This module is testing this process.

    Please refer to the module shared_methods.py for a detailed explanation.
"""

from food_items.openfoodfacts.shared_methods import DataCleaning
from django.test import TestCase
import os
import json


class TestDataCleaning(TestCase, DataCleaning):

    def test_check_special_characters(self):
        values = ["",
                  "le-magasin",
                  "l'autre magasin"]
        test_list = []
        for value in values:
            result = self._check_special_characters(value)
            test_list.append(result)
        self.assertIsNotNone(result)
        self.assertEqual(test_list, ["NaN", "le magasin", "l\'autre magasin"])

    def test_from_data_to_list(self):
        current_path = os.path.abspath(os.getcwd())
        with open(os.path.join(current_path,
                  "food_items/openfoodfacts/tests/off_data_to_be_tested/mock_stores.json"),
                  'r') as f:
            data = json.load(f)
        key_file = "tags"
        key_item = "name"
        store_list = self.from_data_to_list(data, key_file, key_item)
        self.assertGreater(len(store_list), 10)
        return store_list

    def test_assign_url(self):
        values = ["", "null", "https://test_url.com"]
        test_url = self.assign_url(values[0])
        self.assertEqual(test_url,
        "https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-178x150.png")
        test_url = self.assign_url(values[1])
        self.assertEqual(test_url,
        "https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-178x150.png")
        test_url = self.assign_url(values[2])
        self.assertEqual(test_url, "https://test_url.com")

