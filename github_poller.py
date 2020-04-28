#! /usr/bin/env python3
import os
import requests
import asyncio
import argparse
from dotenv import load_dotenv
import sys
from pprint import pprint
from data_parser import ResponseParser

load_dotenv()

API = 'https://api.github.com'
GIT_USER = os.getenv('GIT_USER')
GIT_PASSWORD = os.getenv('GIT_PASSWORD')
print(GIT_USER, GIT_PASSWORD)
session = requests.Session()
session.auth = (GIT_USER, GIT_PASSWORD)


def parse_args():
    """
    The argument parser from the command line
    """

    parser = argparse.ArgumentParser()

    # Add optional (use nargs = ?, otherwise it will be necessary) argument in command line
    parser.add_argument('-user', nargs='?',
                        help='Github username you would like to search for',
                        default=None)

    return parser.parse_args()


def main():

    args = parse_args()
    user = args.user
    if not user:
        print(f'Please specify user you would like to search for using -user')
        sys.exit(1)

    response = session.get(API)
    response.raise_for_status()
    print(f'API check: {response.status_code}')

    user_repos_url = f"{API}/users/{user}/repos?page=100&per_page=20"
    repos_response = session.get(user_repos_url)
    repos_response.raise_for_status()
    print(f'Fetching repos for github user: {user}, {repos_response.status_code, repos_response.text}')

    repos_response = repos_response.json()

    pprint(repos_response, indent=2)

    if repos_response:
        useful_keys = ['full_name', 'archived', 'id', 'url', 'updated_at', 'language']
        useful_data = ResponseParser(response=repos_response, metadata_keys=['language'])
        useful_data.grab_useful_data()

        print(useful_data.most_popular_attribute_value('language'))


if __name__ == '__main__':
    main()