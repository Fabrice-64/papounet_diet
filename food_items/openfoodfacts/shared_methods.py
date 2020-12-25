"""
    Open Food Facts Data need to be cleaned and prepared up
    iot avoid exceptions while uploading.
    This is the purpose of this module.

    Classes:
        DataCleaning: contains all the required methods
        for a nice data preparation.

    Exceptions:
        NIL

    Functions:
        NIL
"""


class DataCleaning():
    """
        Prepare the data before upload.

        Methods:
            _check_special_characters:
            remove all signs which may provoke exceptions.

            _from_data_to_list: 
            self explanatory

            from_string_into_list: 
            self explanatory

            assign_url:
            used when the uploaded data do not have a picture.
            It is then replaced by a logo stored locally.
    """

    def _check_special_characters(self, value):
        """
            Cleans the fields of the downloaded rows iot avoid conflicts
            with DB syntax
            Arguments:
                value: is a string to be checked.
            Returns:
                result: value cleaned from the various quotation marks
                or identified as empty.
        """
        if value is None or value == "":
            cleaned_value = "NaN"
        else:
            if '"' in value:
                value = value.replace('"', '')
            if "'" in value:
                value = value.replace("'", "\'")
            if "-" in value:
                value = value.replace("-", " ")
            if "'" in value:
                value.replace("\xc3\xa9", "é'")
            cleaned_value = value
        return cleaned_value

    def from_data_to_list(self, data, key_file, key_item):
        """
            Used to transfer stores categories from a string to a list.

            Arguments:
                data: takes over a json file
                key_file: to get all the pairs key-value required
                key_item: to get item by item from the key_file.

            Returns:
                list_items: a list of all isolated items.
        """
        list_items = []
        items = data.get(key_file)
        for item in items:
            item = self._check_special_characters(item.get(key_item))
            item = item.strip()
            if item != "NaN":
                list_items.append(item)
        return list_items

    def from_string_into_list(self, string_to_convert):
        if string_to_convert is not None:
            data = string_to_convert.split(",")
            data = [item.strip() for item in data]
        else:
            data = [""]
        return data

    def assign_url(self, url_to_assign):
        # may be redundant with the model. Useful to check if still needed.
        if url_to_assign is None or url_to_assign in ["", "null"]:
            assigned_url = "https://static.openfoodfacts.org/images/misc/openfoodfacts-logo-en-178x150.png"
        else:
            assigned_url = url_to_assign
        return assigned_url
