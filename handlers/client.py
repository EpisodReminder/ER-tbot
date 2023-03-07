import random

from aiogram import types, Dispatcher
from aiogram.dispatcher.filters.state import State, StatesGroup
from aiogram.types import ReplyKeyboardRemove
from keyboards import create_unsubscribe_keyboard, create_keyboard_main, create_keyboard_register
from create_bot import loc

serials_list = [
    'Очень странные дела (Stranger Things)',
    'Игра престолов (Game of Thrones)',
    'Шерлок (Sherlock)',
    'Черное зеркало (Black Mirror)',
    'Друзья (Friends)',
    'Во все тяжкие (Breaking Bad)',
    'Ведьмак (The Witcher)',
    'Бумажный дом (La Casa de Papel)',
    'Мистер Робот (Mr. Robot)',
    'Крутой Сэм (Samurai Jack)',
    'Военный госпиталь (M*A*S*H)',
    'Звездные войны: Повстанцы (Star Wars Rebels)',
    'Мир Дикого запада (Westworld)',
    'Ходячие мертвецы (The Walking Dead)',
    'Доктор Кто (Doctor Who)',
    'Лучше звоните Солу (Better Call Saul)',
    'Парки и зоны отдыха (Parks and Recreation)',
    'Секретные материалы (The X-Files)',
    'Американская история ужасов (American Horror Story)',
    'Дневники вампира (The Vampire Diaries)'
]

BASE_URL = "https://EpisodeRemainder.ru/api"


class FSMClient(StatesGroup):
    main = State()
    subscribe = State()
    unsubscribe = State()


async def hello_handler(message: types.Message):
    locale = message.from_user.language_code
    await FSMClient.main.set()
    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['welcome']}",
        reply_markup=create_keyboard_register(locale))


async def back_handler(message: types.Message):
    locale = message.from_user.language_code
    await FSMClient.main.set()
    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['back']}",
        reply_markup=create_keyboard_register(locale))


async def get_code_handler(message: types.Message):
    locale = message.from_user.language_code
    await message.answer(
        text=f"{BASE_URL}/login/get-confirmation-key?id={str(message.from_user.id)}")
    await message.answer(
        text=f"{random.Random().randint(100000, 999999)}",
        reply_markup=create_keyboard_register(locale))


async def sign_in_handler(message: types.Message):
    locale = message.from_user.language_code
    await message.answer(
        text=f"{BASE_URL}/login/sign-in/?id={str(message.from_user.id)}")
    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['sign_in']}",
        reply_markup=create_keyboard_main(locale))


async def subscribe_select_handler(message: types.Message):
    locale = message.from_user.language_code
    await FSMClient.subscribe.set()
    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['subscribe_select']}",
        reply_markup=ReplyKeyboardRemove())


async def subscribe_handler(message: types.Message):
    locale = message.from_user.language_code
    await FSMClient.main.set()
    await message.answer(
        text=f"{BASE_URL}/subscribes/follow/?series={message.text}&id={str(message.from_user.id)}")
    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['subscribe']}{message.text}",
        reply_markup=create_keyboard_main(locale))


async def get_subscribes_list_handler(message: types.Message):
    locale = message.from_user.language_code
    await message.answer(
        text=f"{BASE_URL}/subscribes/list&id={str(message.from_user.id)}")
    await message.answer(
        text=str('\n'.join(serials_list)),
        reply_markup=create_keyboard_main(locale))


async def unsubscribe_select_handler(message: types.Message):
    await FSMClient.unsubscribe.set()
    await message.answer(
        text=f"{BASE_URL}/subscribes/list&id={str(message.from_user.id)}")
    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['unsubscribe_select']}",
        reply_markup=create_unsubscribe_keyboard(serials_list))


async def unsubscribe_handler(message: types.Message):
    locale = message.from_user.language_code
    await FSMClient.main.set()
    await message.answer(
        text=f"{BASE_URL}/unfollow/&serials={message.text}&id={str(message.from_user.id)}")
    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['unsubscribe']} {message.text}",
        reply_markup=create_keyboard_main(locale))


async def unsubscribe_all_handler(message: types.Message):
    locale = message.from_user.language_code
    await message.answer(
        text=f"{BASE_URL}/unfollow/all/?&id={str(message.from_user.id)}")

    await message.answer(
        text=f"{loc[str(message.from_user.language_code)]['unsubscribe_all']}",
        reply_markup=create_keyboard_main(locale))


def register_client_handlers(dp: Dispatcher):
    dp.register_message_handler(hello_handler, commands=["start"])
    dp.register_message_handler(get_code_handler, check_command("get_code_button"), state=FSMClient.main)
    dp.register_message_handler(sign_in_handler, check_command("sign_in_button"), state=FSMClient.main)
    dp.register_message_handler(get_subscribes_list_handler, check_command("get_subscribes_list_button"),
                                state=FSMClient.main)
    dp.register_message_handler(unsubscribe_select_handler, check_command("unsubscribe_button"), state=FSMClient.main)
    dp.register_message_handler(unsubscribe_all_handler, check_command("unsubscribe_all_button"), state=FSMClient.main)
    dp.register_message_handler(subscribe_select_handler, check_command("subscribe_button"), state=FSMClient.main)
    dp.register_message_handler(back_handler, check_command("back_button"), state=FSMClient.main)
    dp.register_message_handler(unsubscribe_handler, state=FSMClient.unsubscribe)
    dp.register_message_handler(subscribe_handler, state=FSMClient.subscribe)


def check_command(command):
    return lambda x: x.text in loc.get_key_all_languages(command)
