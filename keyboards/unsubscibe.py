from aiogram.types import KeyboardButton, ReplyKeyboardMarkup


def create_unsubscribe_keyboard(serials_list):
    keyboard_unsubscribe = ReplyKeyboardMarkup(resize_keyboard=True)
    for serial in serials_list:
        button_unsubscribe = KeyboardButton(serial)
        keyboard_unsubscribe.row(button_unsubscribe)
    return keyboard_unsubscribe
