#! /usr/bin/env python3
from collections import Counter


class ResponseParser:

    """
    Takes in response data from the Github API and extracts only the attributes specified by the response_attrs arg
    It assembles this parsed data in the metadata property.
    """

    def __init__(self, response, response_attrs):
        if response:
            self.response = response
        else:
            raise ValueError('Empty response')
        self.response_attrs = response_attrs
        self.data = []

    def check_missing_attrs_in_response(self):

        """
        Validation check to ensure that all the response_attrs are present in the API response. This should catch
        misspellings or attributes that have been removed in subsequent versions of the Github API
        """

        unique_keys = [key for repos in self.response for key in repos.keys()]
        unique_attrs = list(set(unique_keys))
        not_found = [attr for attr in self.response_attrs if attr not in unique_attrs]
        return not_found

    def parse_useful_data(self):

        """
        For all repos, extract only the data for the keys specified in response_attrs.
        """

        missing_response_attrs = self.check_missing_attrs_in_response()

        if missing_response_attrs:
            raise ValueError(f'These attrs not found in response: {missing_response_attrs}')

        # Iterate through response and keep the key value pairs specified in response_attrs
        for repo in self.response:
            parsed_data = {}
            for key in self.response_attrs:
                parsed_data[key] = repo.get(key)

            self.data.append(parsed_data)

    def most_popular_attribute_value(self, attribute):

        """
        Work out the most popular values for the given attribute
        attribute: Key found in the API response (and parsed into the metadata property)
        """

        # Check attribute is in parsed data list
        if attribute not in self.response_attrs:
            raise ValueError('Attribute not in parsed data')

        self.parse_useful_data()

        attr_values = [data[attribute] for data in self.data]
        counter = Counter(attr_values)
        most_popular_values = [k for k, v in counter.items() if v == max(counter.values())]

        return most_popular_values


