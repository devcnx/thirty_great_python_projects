import os

MESSAGES = {
    'welcome': f'''
    Welcome to the Image Downloader!

    This application allows you to download images from the web.
    Enter the URL of the image you want to download and the name of the file you want to save it as.
    Images will be stored in the 'images' folder in the current directory.

    Let's get started!
    ''',

    'checking_dir': '\nChecking For the Images Directory...',
    'creating_dir': '\nCreating the Images Directory...',
    'checking_for_image': '\nChecking For the Image...''',
    'saving': '\nSaving Image...''',
    'downloading': '\nDownloading Image...''',

    'invalid_input': '\t*** Invalid Input. Please Try Again...''',
    'invalid_image_ext': '\t*** Invalid File Extension. Please Try Again...',
    'invalid_url': '\t*** Invalid URL. Please Try Again...',
    'image_saved': 'Image Saved Successfully!',
    'image_downloaded': 'Image Downloaded Successfully!',

    'try_again': '\nWould You Like to Download Another Image? (Y/N): ',
    'exit': '\nThanks for Using the Image Downloader!\nGoodbye!'
}
IMAGES_DIR = os.path.join(os.path.dirname(__file__), 'images')
VALID_EXTENSIONS = ['.png', '.jpg', '.jpeg', '.gif', '.svg', '.ico']
