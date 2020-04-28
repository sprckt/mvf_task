#! /usr/bin/env python3
import os
import requests
import asyncio
import argparse
from dotenv import load_dotenv
import sys
from pprint import pprint

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

    test_url = API
    response = session.get(API)
    response.raise_for_status()

    print(f'Fetching repos for github user: {user}')
    pprint(response.json(), indent=2)


if __name__ == '__main__':
    main()