#! /usr/bin/env python3
import os
import requests
import argparse
from dotenv import load_dotenv
import sys
from data_parser import ResponseParser

# Environment and config vars
load_dotenv()
API = 'https://api.github.com'
GIT_USER = os.getenv('GIT_USER')
GIT_PASSWORD = os.getenv('GIT_PASSWORD')

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

    # Grab command line args
    args = parse_args()
    user = args.user
    if not user:
        print(f'Specify github username using -user argument')
        sys.exit(1)

    all_repos = []
    repos_response = True
    page_num = 1
    while repos_response:

        # Generate URL and poll API
        user_repos_url = f"{API}/users/{user}/repos?page={page_num}&per_page=50"
        try:
            repos_response = session.get(user_repos_url)
            repos_response.raise_for_status()
        except requests.exceptions.HTTPError as e:
            print(f'Check API is available and user name is correct: {e}')
            sys.exit(1)

        # Convert to JSON
        repos_response = repos_response.json()
        print(f'Fetched repos for github user {user}, page {page_num}: {len(repos_response)}')

        # Add only if populated response comes back
        if repos_response:
            all_repos.extend(repos_response)
        page_num += 1

    # The response attributes to parsed out
    useful_keys = ['full_name', 'language', 'url', 'watchers']

    # Parse all response data to ResponseParser to work out most popular language.
    parsed_data = ResponseParser(response=all_repos, response_attrs=useful_keys)
    parsed_data.parse_useful_data()
    popular = parsed_data.most_popular_attribute_value('language')

    # Output from analysis
    print(f'For user {user}, popular languages are: {popular}')


if __name__ == '__main__':
    main()
