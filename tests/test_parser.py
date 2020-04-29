#! /usr/bin/env python3
import pytest
from data_parser import ResponseParser


def test_empty_response(empty_response):

    with pytest.raises(ValueError):
        parsed_data = ResponseParser(response=empty_response, response_attrs=['name', 'language'])


def test_missing_attrs_in_response(single_popular_language):

    parsed_attrs = ['name', 'language', 'author']
    parsed_data = ResponseParser(response=single_popular_language, response_attrs=parsed_attrs)
    with pytest.raises(ValueError):
        parsed_data.parse_useful_data()


def test_single_popular_language(single_popular_language):

    parsed_data = ResponseParser(response=single_popular_language, response_attrs=['name', 'language'])
    popular = parsed_data.most_popular_attribute_value(attribute='language')

    assert popular == ['Python']


def test_multiple_popular_languages(multiple_popular_language):

    parsed_data = ResponseParser(response=multiple_popular_language, response_attrs=['name', 'language'])
    popular = parsed_data.most_popular_attribute_value(attribute='language')

    assert popular == ['Python', 'Ruby']