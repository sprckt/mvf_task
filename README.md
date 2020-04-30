# MVF Recruitment Task

##  Introduction
This project contains the recruitment task for MVF. The task required polling the Github API for a user's repositories
 to evaluate the most popular programming language. The project relies on Python3.7 and the following libraries:
- requests
- python-dotenv
- pytest

The project consists of two main files and is a command line application:
- github_poller.py: Packages up the request to the Github API
- data_parser.py: Reads in the data and extracts out useful information
 
## Getting Started

1. Environment variables, config and secrets 
Should all be stored in .env file at the root of the project. This is
 exposed to the github_poller.py at run time. As a minimum the file should contain the following variables
```.env
GIT_USER=
GIT_PASSWORD=
```
The GIT_PASSWORD variable should be a generated personal access token (not your password, which will not work if you
 have MFA set up). 
For instructions on set up look [here](https://help.github.com/en/github/authenticating-to-github/creating-a-personal-access-token-for-the-command-line)

2. Build and run
The project is containerised using Docker. Commands are wrapped up in a Makefile for ease of use.

```.env
# Build image
make build

# Run app for github user 'facebook'
make GIT_USER=facebook run
```

3. Tests
Unit tests use the pytest framework. To run tests use:
```.env
# Run tests
make test
```

4. Expected output
A successful run of the app should give you the following type of output. If there are multiple-languages that
 are the most popular, all languages will be returned in the list.   
`For user aws, popular languages are: ['Python']`

## Developer Notes

As the expected response and the number of calls to the Github API was relatively small, the decision was made to
 develop this application using the synchronous requests library. If the project had required a large number of
  requests, then an alternative approach using the python asynchronous libraries asyncio and aiohttp would have been used. 

Currently the project uses the collections.Counter() object to return a frequency count of all the languages, it then
 does another parse through this Counter() object to extract the languages with the highest count. In Python 3.8 this
  operation could be much simpler using the statistics.multimodal() method to return the most popular languages from
   the original languages list. One for future improvement!


## Future Development
This command line app could be readily turned into a web app. For such a simple case, Flask seems an appropriate fit
 (and the web framework I've had most recent experience with). For more significant analysis, the pandas library
  would be useful - but does inflate the project build significantly.
  