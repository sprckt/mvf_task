#! /usr/bin/env python3
import pytest
from data_parser import ResponseParser


def test_empty_response(empty_response):

    # Test how the ResponseParser deals with an empty response from API

    with pytest.raises(ValueError):
        parsed_data = ResponseParser(response=empty_response, response_attrs=['name', 'language'])


def test_missing_attrs_in_response(single_popular_language):

    # A  missing attribute in the parsed data dictionary should raise a ValueError

    parsed_attrs = ['name', 'language', 'author']
    parsed_data = ResponseParser(response=single_popular_language, response_attrs=parsed_attrs)
    with pytest.raises(ValueError):
        parsed_data.parse_useful_data()


def test_single_popular_language(single_popular_language):

    # Test to see if a single popular language is returned

    parsed_data = ResponseParser(response=single_popular_language, response_attrs=['name', 'language'])
    popular = parsed_data.most_popular_attribute_value(attribute='language')

    assert popular == ['Python']


def test_multiple_popular_languages(multiple_popular_language):

    # Test to see if multiple popular languages are returned

    parsed_data = ResponseParser(response=multiple_popular_language, response_attrs=['name', 'language'])
    popular = parsed_data.most_popular_attribute_value(attribute='language')

    assert popular == ['Python', 'Ruby']