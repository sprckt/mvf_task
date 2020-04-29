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

    # Github username
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

    all_repos = []
    repos_response = True
    page_num = 1
    while repos_response:
        user_repos_url = f"{API}/users/{user}/repos?page={page_num}&per_page=50"
        repos_response = session.get(user_repos_url)
        repos_response.raise_for_status()

        repos_response = repos_response.json()
        print(f'Fetched repos for github user {user}, page {page_num}: {len(repos_response)}')

        # pprint(repos_response, indent=2)
        if repos_response:
            all_repos.extend(repos_response)
        page_num += 1

    response_lengths = set(len(repo) for repo in all_repos)
    print(f'Repo sizes: {response_lengths}')
    useful_keys = ['full_name', 'language', 'url', 'watchers']
    parsed_data = ResponseParser(response=all_repos, response_attrs=useful_keys)
    parsed_data.parse_useful_data()
    popular = parsed_data.most_popular_attribute_value('language')
    print(f'For user {user}, popular languages are: {popular}')


if __name__ == '__main__':
    main()