from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallBack(CallbackData, prefix="main"):
    menu_name: str
    level: int | None = None
    # image_id: int | None = None


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Старт квиза 🍕": "season",
        "Результат 🛒": "result",
        "О боте ℹ️": "about_b",
        "О нас 💰": "about",
    }
    for text, menu_name in btns.items():
        if menu_name == 'season':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=10, menu_name='season').pack()))
        elif menu_name == 'result':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=1, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()


class SeasonCallBack(CallbackData, prefix="season"):
    menu_name: str
    level: int | None = None


def get_user_season_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Зима": "winter",
        "Весна": "spring",
        "Лето": "summer",
        "Осень": "autumn",
        "Назад": "start",
    }
    for text, menu_name in btns.items():
        if menu_name == 'start':
            keyboard.add(InlineKeyboardButton(text='Назад',
                                              callback_data=MenuCallBack(level=0, menu_name='main').pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=level, menu_name=menu_name).pack()))
    return keyboard.adjust(*sizes).as_markup()
