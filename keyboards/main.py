from aiogram.types import KeyboardButton, ReplyKeyboardMarkup
from create_bot import loc


def create_keyboard_main(language):
    keyboard_main = ReplyKeyboardMarkup(resize_keyboard=True)
    button_get_subscribes_list = KeyboardButton(loc[language]["get_subscribes_list_button"])
    button_subscribe = KeyboardButton(loc[language]["subscribe_button"])
    button_unsubscribe = KeyboardButton(loc[language]["unsubscribe_button"])
    button_unsubscribe_all = KeyboardButton(loc[language]["unsubscribe_all_button"])
    button_back = KeyboardButton(loc[language]["back_button"])
    keyboard_main.row(button_get_subscribes_list, button_subscribe)
    keyboard_main.row(button_unsubscribe, button_unsubscribe_all)
    keyboard_main.row(button_back)
    return keyboard_main
