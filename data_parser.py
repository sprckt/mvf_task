#! /usr/bin/env python3
from collections import Counter
import statistics


class ResponseParser:

    def __init__(self, response, response_attrs):
        if response:
            self.response = response
        else:
            raise ValueError('Empty response')
        self.response_attrs = response_attrs
        self.metadata = []

    def check_missing_attrs_in_response(self):

        unique_keys = [key for repos in self.response for key in repos.keys()]
        unique_attrs = list(set(unique_keys))
        not_found = [attr for attr in self.response_attrs if attr not in unique_attrs]
        return not_found

    def parse_useful_data(self):

        missing_response_attrs = self.check_missing_attrs_in_response()

        if missing_response_attrs:
            raise ValueError(f'These attrs not found in response: {missing_response_attrs}')

        # Iterate through response and keep the key value pairs specified in response_attrs
        for repo in self.response:
            parsed_data = {}
            for key in self.response_attrs:
                parsed_data[key] = repo.get(key)

            self.metadata.append(parsed_data)

    def most_popular_attribute_value(self, attribute):

        # Edge cases
        # Key not in attribute list
        if attribute not in self.response_attrs:
            raise ValueError('Attribute not in parsed data')

        self.parse_useful_data()

        attr_values = [data[attribute] for data in self.metadata]
        counter = Counter(attr_values)
        most_popular_values = [k for k, v in counter.items() if v == max(counter.values())]


        return most_popular_values

