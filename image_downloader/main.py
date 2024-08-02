"""
Image Downloader. 

This script allows users to download images from URLs. It provides a command-line interface for users to input
image URLs and desired file names, then downloads and saves the images to the specified directory. 
"""
import os
import requests
from constants import MESSAGES, IMAGES_DIR, VALID_EXTENSIONS
from typing import Optional


def get_user_input(prompt: str) -> str:
    """
    Prompt the user for input and return the stripped response. 

    Parameters:
        prompt: The prompt to display to the user.
        :type prompt: str

    Returns:
        The user's input.
        :rtype: str
    """
    return input(prompt).strip()


def is_valid_url(url: str) -> bool:
    """
    Check if the given URL contains a valid image extension.

    Parameters:
        url: The URL to check.
        :type url: str

    Returns:
        True if the URL ends with a valid image extension, False otherwise. 
        :rtype: bool
    """
    return get_extension(url) in VALID_EXTENSIONS


def get_response(url: str) -> Optional[requests.Response]:
    """
    Send an HTTP GET request to the given URL and return the response.

    Parameters:
        url: The URL to send the request to.
        :type url: str

    Returns:
        The response from the request, or None if the request failed.
        :rtype: Optional[requests.Response]
    """
    try:
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        return response
    except requests.exceptions.RequestException:
        return None


def set_protocol(url: str) -> str:
    """
    Ensure the URL has a protocol prefix, defaulting to HTTPS if none is present. 

    Parameters:
        url: The URL to check.
        :type url: str

    Returns:
        The URL with a protocol prefix, or the original URL if a protocol prefix is already present.
        :rtype: str
    """
    return url if url.startswith(('http://', 'https://')) else f'https://{url}'


def download_image(url: str, image_name: str) -> bool:
    """
    Download an image from the given URL and save it with the specified name.

    Parameters:
        url: The URL of the image to download.
        :type url: str

        image_name: The name of the image file to save.
        :type image_name: str

    Returns:
        True if the image was downloaded successfully, False otherwise.
    """
    response = get_response(url)
    if not response:
        print(MESSAGES['invalid_url'])
        return False
    try:
        with open(os.path.join(IMAGES_DIR, image_name), 'wb') as image:
            image.write(response.content)
            print(MESSAGES['image_saved'])
            return True
    except IOError:
        print(MESSAGES['invalid_image_ext'])
        return False


def get_extension(url: str) -> Optional[str]:
    """
    Extract the file extension from the given URL.

    Parameters:
        url: The URL to extract the extension from.
        :type url: str

    Returns:
        The file extension of the URL, or None if the URL does not have an extension.
        :rtype: Optional[str]
    """
    for extension in VALID_EXTENSIONS:
        if extension in url:
            return extension
    return None


def main() -> None:
    """
    The main function to run the image downloader. 

    This function handles the main loop of the program, prompting the user for input, validating
    the input, and initiating the image download process. 

    Returns:
        None
    """
    print(MESSAGES['welcome'])
    while True:
        url = get_user_input('\nEnter the URL of the Image to Download: ')
        if not url:
            print(MESSAGES['invalid_input'])
            continue

        url = set_protocol(url)

        if not is_valid_url(url):
            print(MESSAGES['invalid_url'])
            continue

        extension = get_extension(url)
        if not extension:
            print(MESSAGES['invalid_url'])
            continue

        image_name = get_user_input(f'Enter the Name of the File to Save ({url.split("/")[-1]}): ')
        if not image_name:
            print(MESSAGES['invalid_input'])
            continue
        image_name = f'{image_name}{extension}'
        if download_image(url, image_name):
            print(MESSAGES['image_downloaded'])
        else:
            continue

        try_again = get_user_input(MESSAGES['try_again'])
        if not try_again or try_again.lower() not in ['y', 'n']:
            print(MESSAGES['invalid_input'])
            continue
        if try_again.lower() == 'n':
            break
        else:
            continue

    print(MESSAGES['exit'])


if __name__ == '__main__':
    main()
