from aiogram.filters.callback_data import CallbackData
from aiogram.types import InlineKeyboardButton
from aiogram.utils.keyboard import InlineKeyboardBuilder


class MenuCallBack(CallbackData, prefix="main"):
    menu_name: str
    level: int | None = None


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
        elif menu_name == 'winter':
            keyboard.add(InlineKeyboardButton(text="Зима",
                                              callback_data=MenuCallBack(level=20, menu_name='amount').pack()))
        elif menu_name == 'spring':
            keyboard.add(InlineKeyboardButton(text="Весна",
                                              callback_data=MenuCallBack(level=20, menu_name='amount').pack()))
        elif menu_name == 'summer':
            keyboard.add(InlineKeyboardButton(text="Лето",
                                              callback_data=MenuCallBack(level=20, menu_name='amount').pack()))
        elif menu_name == 'autumn':
            keyboard.add(InlineKeyboardButton(text="Осень",
                                              callback_data=MenuCallBack(level=20, menu_name='amount').pack()))
    return keyboard.adjust(*sizes).as_markup()


def get_user_amount_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Только в 2м": "two",
        "Только близкие": "folks",
        "До ста": "up_to_100",
        "Больше 100": "more_than_100",
        "Назад": "start2",
    }
    for text, menu_name in btns.items():
        if menu_name == "start2":
            keyboard.add(InlineKeyboardButton(text='Назад',
                                              callback_data=MenuCallBack(level=10, menu_name='season').pack()))
        elif menu_name == 'two':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=30, menu_name='place').pack()))
        elif menu_name == 'folks':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=30, menu_name='place').pack()))
        elif menu_name == 'up_to_100':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=30, menu_name='place').pack()))
        elif menu_name == 'more_than_100':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=30, menu_name='place').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_place_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "В саду": "garden",
        "Ресторан": "restaurant",
        "На берегу моря": "sea",
        "Уникальное место": "unique",
        "Назад": "start3",
    }
    for text, menu_name in btns.items():
        if menu_name == "start3":
            keyboard.add(InlineKeyboardButton(text='Назад',
                                              callback_data=MenuCallBack(level=20, menu_name='amount').pack()))
        elif menu_name == 'garden':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=40, menu_name='style').pack()))
        elif menu_name == 'restaurant':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=40, menu_name='style').pack()))
        elif menu_name == 'sea':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=40, menu_name='style').pack()))
        elif menu_name == 'unique':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=40, menu_name='style').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_style_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Классическая": "classic",
        "Эксцентричная": "eccentric",
        "Модерн": "modern",
        "Романтическая": "romantic",
        "Путешествие": "travel",
        "Винтажная": "vintage",
        "Назад": "start4",
    }
    for text, menu_name in btns.items():
        if menu_name == "start4":
            keyboard.add(InlineKeyboardButton(text='Назад',
                                              callback_data=MenuCallBack(level=30, menu_name='place').pack()))
        elif menu_name == 'classic':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=50, menu_name='colors').pack()))
        elif menu_name == 'eccentric':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=50, menu_name='colors').pack()))
        elif menu_name == 'modern':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=50, menu_name='colors').pack()))
        elif menu_name == 'romantic':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=50, menu_name='colors').pack()))
        elif menu_name == 'travel':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=50, menu_name='colors').pack()))
        elif menu_name == 'vintage':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=50, menu_name='colors').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_colors_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Пыльная роза": "dirty_rose",
        "Изумрудно-зеленый": "emerald_green",
        "Капучино": "macchiato",
        "Розовый кварц": "quartz_pink",
        "Ванильный": "vanilla_cream",
        "Винный": "wine",
        "Назад": "start5",
    }
    for text, menu_name in btns.items():
        if menu_name == "start5":
            keyboard.add(InlineKeyboardButton(text='Назад',
                                              callback_data=MenuCallBack(level=40, menu_name='style').pack()))
        elif menu_name == 'dirty_rose':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=60, menu_name='fashion').pack()))
        elif menu_name == 'emerald_green':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=60, menu_name='fashion').pack()))
        elif menu_name == 'macchiato':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=60, menu_name='fashion').pack()))
        elif menu_name == 'quartz_pink':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=60, menu_name='fashion').pack()))
        elif menu_name == 'vanilla_cream':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=60, menu_name='fashion').pack()))
        elif menu_name == 'wine':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=60, menu_name='fashion').pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_fashion_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Трапециевидный силуэт": "trapezoidal",
        "Русалка": "naiad",
        "Футляр": "sheath",
        "Бальное платье": "ball_gown",
        "Комбинезон": "overalls",
        "Ретро": "retro",
        "Назад": "start6",
    }
    for text, menu_name in btns.items():
        if menu_name == "start6":
            keyboard.add(InlineKeyboardButton(text='Назад',
                                              callback_data=MenuCallBack(level=50, menu_name='colors').pack()))
        elif menu_name == 'trapezoidal':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=70, menu_name="costume").pack()))
        elif menu_name == 'naiad':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=70, menu_name="costume").pack()))
        elif menu_name == 'sheath':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=70, menu_name="costume").pack()))
        elif menu_name == 'ball_gown':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=70, menu_name="costume").pack()))
        elif menu_name == 'overalls':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=70, menu_name="costume").pack()))
        elif menu_name == 'retro':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=70, menu_name="costume").pack()))

    return keyboard.adjust(*sizes).as_markup()


def get_user_costume_btns(*, level: int, sizes: tuple[int] = (2,)):
    """ Инлайн билдер клавиатуры со словарем ключ значение"""
    keyboard = InlineKeyboardBuilder()
    btns = {
        "Классика": "classic_costume",
        "Смокинг": "tuxedo",
        "Кэжуал": "casual",
        "Современный костюм": "modern_costume",
        "Назад": "start7",
    }
    for text, menu_name in btns.items():
        if menu_name == "start7":
            keyboard.add(InlineKeyboardButton(text='Назад',
                                              callback_data=MenuCallBack(level=60, menu_name='fashion').pack()))
        elif menu_name == 'classic_costume':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=0, menu_name='main').pack()))
        elif menu_name == 'tuxedo':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=0, menu_name='main').pack()))
        elif menu_name == 'casual':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=0, menu_name='main').pack()))
        elif menu_name == 'modern_costume':
            keyboard.add(InlineKeyboardButton(text=text,
                                              callback_data=MenuCallBack(level=0, menu_name='main').pack()))
    return keyboard.adjust(*sizes).as_markup()
