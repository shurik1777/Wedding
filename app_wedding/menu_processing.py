from aiogram.types import InputMediaPhoto
from sqlalchemy.ext.asyncio import AsyncSession

from app_wedding.database.orm_query import orm_get_banner
from app_wedding.kbds.inline import get_user_main_btns


async def main_menu(session, level, menu_name):
    banner = await orm_get_banner(session, menu_name)
    image = InputMediaPhoto(media=banner.image, caption=banner.description)

    kbds = get_user_main_btns(level=level)

    return image, kbds


async def get_menu_content(
    session: AsyncSession,
    menu_name: str,
    level: int,
    category: int | None = None,
    page: int | None = None,
    product_id: int | None = None,
    user_id: int | None = None,
):
    if level == 0:
        return await main_menu(session, level, menu_name)
    # elif level == 1:
    #     return await catalog(session, level, menu_name)
    # elif level == 2:
    #     return await products(session, level, category, page)
    # elif level == 3:
    #     return await carts(session, level, menu_name, page, user_id, product_id)