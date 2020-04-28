#! /usr/bin/env python3
from collections import Counter


class ResponseParser:

    def __init__(self, response, metadata_keys):
        self.response = response
        self.metadata_keys = metadata_keys
        self.metadata = []

    def grab_useful_data(self):

        # TODO: Edge cases
        ## Empty response
        ## Metadata keys not in response

        for repo in self.response:
            parsed_data = {}
            for key in self.metadata_keys:
                parsed_data[key] = repo.get(key)

            self.metadata.append(parsed_data)

    def most_popular_attribute_value(self, key):

        # Edge cases
        # Key not in attribute list

        self.grab_useful_data()

        attr_values = [data[key] for data in self.metadata]
        counter = Counter(attr_values)

        most_popular_count = max(counter.values())

        most_popular_values = [k for k, v in counter.items() if v == most_popular_count]

        return most_popular_values

