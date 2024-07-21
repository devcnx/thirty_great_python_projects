"""
Website Checker. 

This module contains the code for the website checker. The website checker is a tool that allows users to check the 
status of websites. The user can enter a list of websites in a CSV file, and the website checker will check the status
of each website and print the results. It's designed to be run from the command line. 

The module imports the csv, os, requests, fake_useragent, and http modules. The csv module is used to read and write
CSV files. The os module is used to interact with the operating system. The requests module is used to send HTTP
requests. The fake_useragent module is used to generate fake user agents. The http module is used to get the status
code of a website. 

The application also imports the constants module, which contains the WEBSITE_CSV_FILE constant. The WEBSITE_CSV_FILE
constant is the name of the CSV file that contains the list of websites to check. The application contains functions
for getting or creating the CSV file, getting the list of websites, getting the user agent, and getting the status
description of a website. 
"""
import csv
import os
import requests
from constants import WEBSITE_CSV_FILE
from fake_useragent import UserAgent
from http import HTTPStatus


def get_or_create_csv_file() -> open:
    """
    Get or create the CSV file. 

    This function gets the CSV file, if it exists. If it doesn't exist, the CSV file is created and opened
    with write access. The function returns the CSV file back to the caller. The function takes no parameters. 

    Returns:
        The CSV file. 
        :rtype: open
    """
    if not os.path.exists(WEBSITE_CSV_FILE):
        with open(WEBSITE_CSV_FILE, 'w'):
            pass
    return open(WEBSITE_CSV_FILE, 'a')


def get_websites() -> list:
    """
    Get the list of websites. 

    This function gets the list of websites from the CSV file. The function takes no parameters. It uses
    the csv module to read the CSV file and append 'https://' to each website if it doesn't already have it.
    Otherwise, it just appends the website to the list. The function returns the list of websites back to the
    caller. 

    Returns:
        The list of websites.
        :rtype: list
    """
    websites = []
    with open(WEBSITE_CSV_FILE, 'r') as csv_file:
        reader = csv.reader(csv_file)
        for row in reader:
            if 'https://' not in row[1]:
                websites.append(f'https://{row[1]}')
            else:
                websites.append(row[1])
    return websites


def get_user_agent() -> str:
    """
    Get the user agent. 

    This function is used to get the user agent. The user agent is a string that contains information about the 
    browser, operating system, and device. The function takes no parameters. It uses the fake_useragent module
    to generate a fake user agent. The function returns the user agent back to the caller for use in the check_website
    function.

    Returns:
        The user agent.
        :rtype: str
    """
    ua = UserAgent()
    return ua.chrome


def get_status_description(status_code: int) -> str:
    """
    Get the status description. 

    This function is used to get the status description. The status description is a string that contains information
    about the status code. The function takes one parameter, which is the status code. It uses the HTTPStatus module
    to get the status description from the code. The function returns the description back to the caller as
    a string. 

    Parameters:
        status_code: The status code. 
        :type status_code: int

    Returns:
        The status description. 
        :rtype: str
    """
    for value in HTTPStatus:
        if value == status_code:
            description: str = f'({value} {value.name}) {value.description}'
            return description
    return '(???) Unknown Status Code'


def check_website(website: str, user_agent: str) -> str:
    """
    Check the website. 

    This function is used to check the website. The function takes two parameters, which are the website and the user
    agent. It uses the requests module to get the status code of the website, and then uses the get_status_description
    function to get the status description. The function returns the status description back to the caller as a 
    string. 

    Parameters:
        website: The website. 
        :type website: str

        user_agent: The user agent.
        :type user_agent: str

    Returns:
        The status description.
        :rtype: str
    """
    try:
        code = requests.get(website, headers={'User-Agent': user_agent}).status_code
        print(website, get_status_description(code))
    except Exception:
        print(f'{" " * 2}*** Could Not Get Information for Website: {website}')


if __name__ == '__main__':
    print(f'\nChecking websites from {WEBSITE_CSV_FILE}...')
    get_or_create_csv_file()
    websites = get_websites()
    user_agent = get_user_agent()
    for index, website in enumerate(websites, start=1):
        print(f'\nChecking website {index} of {len(websites)}: {website}')
        check_website(website, user_agent)
    print('\nDone!')
