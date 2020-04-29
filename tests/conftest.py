#! /usr/bin/env python3
import pytest


@pytest.fixture(scope='module')
def empty_response():
    return []


@pytest.fixture(scope='module')
def single_popular_language():

    return [
        {
            'name': 'fish',
            'archived': True,
            'created_at': '2020-07-11T20:12:26Z',
            'id': 1,
            'language': 'Python',
            'url': 'https://api.github.com/repos/test/fish',
         },
        {
            'name': 'cat',
            'archived': True,
            'created_at': '2019-07-11T20:12:26Z',
            'id': 2,
            'language': 'Ruby',
            'url': 'https://api.github.com/repos/test/cat',
        },
        {
            'name': 'hat',
            'archived': True,
            'created_at': '2020-07-11T20:12:26Z',
            'id': 3,
            'language': 'Python',
            'url': 'https://api.github.com/repos/test/hat',
        },
        {
            'name': 'fox',
            'archived': True,
            'created_at': '2015-07-11T20:12:26Z',
            'id': 4,
            'language': 'C++',
            'url': 'https://api.github.com/repos/test/fox',
        }
    ]


@pytest.fixture(scope='module')
def multiple_popular_language():

    return [
        {
            'name': 'fish',
            'archived': True,
            'created_at': '2020-07-11T20:12:26Z',
            'id': 1,
            'language': 'Python',
            'url': 'https://api.github.com/repos/test/fish',
         },
        {
            'name': 'cat',
            'archived': True,
            'created_at': '2019-07-11T20:12:26Z',
            'id': 2,
            'language': 'Ruby',
            'url': 'https://api.github.com/repos/test/cat',
        },
        {
            'name': 'hat',
            'archived': True,
            'created_at': '2020-07-11T20:12:26Z',
            'id': 3,
            'language': 'Python',
            'url': 'https://api.github.com/repos/test/hat',
        },
        {
            'name': 'fox',
            'archived': True,
            'created_at': '2015-07-11T20:12:26Z',
            'id': 4,
            'language': 'C++',
            'url': 'https://api.github.com/repos/test/fox',
        },
        {
            'name': 'knox',
            'archived': True,
            'created_at': '2015-07-11T20:12:26Z',
            'id': 5,
            'language': 'Ruby',
            'url': 'https://api.github.com/repos/test/fox',
        }
    ]