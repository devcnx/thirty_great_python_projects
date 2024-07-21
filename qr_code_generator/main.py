import qrcode
import os
from constants import QR_CODE_IMAGES_DIRS, QR_CODE_SIZES, COLOR_CODES


def display_welcome() -> None:
    print('''
    Welcome to the QR Code Generator!

    This application allows you to generate QR codes for any input text or URL.
    The generated QR codes can be saved as image files (PNG) for later use.

    Follow the on-screen instructions to enter your choice of text or URL.
    ''')


def display_list(message: str, list_to_display: list) -> None:
    print(message)
    for index, item in enumerate(list_to_display, start=1):
        print(f'  {index}. {item}')
    print()


def get_user_input(prompt: str) -> str:
    return input(prompt)


def is_valid_input(user_input: str) -> bool:
    return user_input != '' and user_input is not None and len(user_input.strip()) >= 3


def is_valid_int(user_input: str) -> bool:
    try:
        int(user_input)
        return True
    except ValueError:
        return False


def is_valid_option(user_input: str, options: list) -> bool:
    return is_valid_int(user_input) and 1 <= int(user_input) <= len(options)


def get_valid_user_input(prompt: str, validation_function) -> str:
    while True:
        user_input = get_user_input(prompt)
        if validation_function(user_input):
            return user_input
        print('  *** Invalid Input. Please Try Again...\n')


def get_user_choice(options: list) -> str:
    return get_valid_user_input('Enter Your Choice: ', lambda user_input: is_valid_option(user_input, options))


def display_user_choice(choice: str, options: list) -> str:
    user_choice = int(choice) - 1
    if user_choice >= 0:
        selected_option = options[user_choice]
        print(f'  Your Choice: {selected_option}')
        return selected_option
    else:
        print('  *** Invalid Choice. Please Try Again...\n')
        return None


def get_number_of_saved_qr_codes() -> int:
    return len(os.listdir(QR_CODE_IMAGES_DIRS)) if os.path.exists(QR_CODE_IMAGES_DIRS) else 0


def generate_qr_code(text: str, size: int, color: str) -> None:
    qr_code = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=size,
        border=4,
    )
    file_name = f'qr_code_{get_number_of_saved_qr_codes() + 1}'.lower()
    qr_code.add_data(text)
    qr_code.make(fit=True)
    qr_code_image = qr_code.make_image(fill_color=color, back_color="white")
    os.makedirs(QR_CODE_IMAGES_DIRS, exist_ok=True)
    qr_code_image.save(f'{QR_CODE_IMAGES_DIRS}{file_name}.png')
    print(f'\n  QR Code Generated Successfully.\n  The Image Has Been Saved As {file_name}.png\n')


def generate_again() -> bool:
    return get_valid_user_input('Would You Like to Generate Another QR Code? (Y/N): ', lambda user_input: user_input.lower() in ['y', 'n']).lower() == 'y'


def display_exit_message() -> str:
    return f'\nThanks for using the QR Code Generator. Goodbye!\n'


if __name__ == '__main__':

    display_welcome()
    while True:
        qr_code_text_or_url = get_user_input('Enter Text or URL: ')
        if not is_valid_input(qr_code_text_or_url):
            print('  *** Invalid Input. Please Try Again...\n')
            continue

        display_list('\nPick Your QR Code Size:', QR_CODE_SIZES)
        qr_code_size_choice = get_user_choice(QR_CODE_SIZES)
        qr_code_size = display_user_choice(qr_code_size_choice, QR_CODE_SIZES)
        if qr_code_size is None:
            continue

        display_list('\nPick Your QR Code Color:', COLOR_CODES)
        qr_code_color_choice = get_user_choice(COLOR_CODES)
        qr_code_color = display_user_choice(qr_code_color_choice, COLOR_CODES)
        if qr_code_color is None:
            continue

        qr_code_color = qr_code_color.split(' (')[0]  # Extract color code

        generate_qr_code(qr_code_text_or_url, int(qr_code_size), qr_code_color)

        if not generate_again():
            print(display_exit_message())
            break
        print()
