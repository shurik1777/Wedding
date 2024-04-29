from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallBack(CallbackData, prefix="main"):
    menu_name: str
    image_id: int | None = None


def get_user_main_btns(*, level: int, sizes: tuple[int] = (2,)):
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Старт квиза 🍕": "quiz",
        "Результат 🛒": "result",
        "О боте ℹ️": "about_b",
        "О нас 💰": "about",
    }
    for text, menu_name in btns.items():
        if menu_name == 'quiz':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=10, menu_name=menu_name).pack()))
        elif menu_name == 'result':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=1, menu_name=menu_name).pack()))
        elif menu_name == 'about_b':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=2, menu_name=menu_name).pack()))
        else:
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=3, menu_name=menu_name).pack()))

    return keyboard.adjust(*sizes).as_markup()