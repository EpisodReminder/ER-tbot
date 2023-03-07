from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from create_bot import loc


def create_keyboard_register(language):
    keyboard_register = ReplyKeyboardMarkup(resize_keyboard=True)
    button_get_code = KeyboardButton(loc[language]["get_code_button"])
    button_sign_in = KeyboardButton(loc[language]["sign_in_button"])
    keyboard_register.row(button_get_code)
    keyboard_register.row(button_sign_in)
    return keyboard_register
