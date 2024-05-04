from aiogram.types import InputMediaPhoto
from sqlalchemy.ext.asyncio import AsyncSession

from app_wedding.database.orm_query import orm_get_banner
from app_wedding.kbds.inline import get_user_main_btns, get_user_season_btns


async def main_menu(session, level, menu_name):
    """ Стартовое меню """
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_main_btns(level=level)

    return image, kbds


async def season(session, level, menu_name):
    """ Второй уровень меню """
    banner = await orm_get_banner(session, menu_name)
    if banner is not None:
        image = InputMediaPhoto(media=banner.image, caption=banner.description)
    else:
        image = None
    kbds = get_user_season_btns(level=level)

    return image, kbds


async def get_menu_content(
        session: AsyncSession,
        menu_name: str,
        level: int,
):
    """ Контент на вывод по уровням (сессия для работы с бд из в,
    левел уровень подтягивания клавиатуры инлайн, название меню строковое значение"""
    if level == 0:
        return await main_menu(session, level, menu_name)
    elif level == 10:
        return await season(session, level, menu_name)
    # elif level == 2:
    #     return await amount(session, level, menu_name)
    # elif level == 3:
    #     return await place(session, level, menu_name)
