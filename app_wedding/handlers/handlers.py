from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from app_wedding.database.models import Quiz
from app_wedding.database.orm_query import orm_add_user
from app_wedding.filters.chat_types import ChatTypeFilter
from app_wedding.kbds.inline import MenuCallBack
from app_wedding.menu_processing import get_menu_content

router = Router()
router.message.filter(ChatTypeFilter(["private"]))


@router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    media, reply_markup = await get_menu_content(session, level=0, menu_name="main")

    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)


async def add_user(callback: types.CallbackQuery, session: AsyncSession):
    user = callback.from_user
    await orm_add_user(
        session,
        user_id=user.id,
    )
    await callback.answer()


async def dell_user(callback: types.CallbackQuery, session: AsyncSession):
    user = callback.from_user
    from sqlalchemy import delete
    query = delete(Quiz).where(Quiz.user_id == user.id)
    await session.execute(query)
    await session.commit()
    await callback.answer()


async def add_values(callback: types.CallbackQuery, session: AsyncSession, values: str):
    user = callback.from_user
    from sqlalchemy import update
    stmt = update(Quiz).where(user.id == Quiz.user_id).values(
        season=values)
    await session.execute(stmt)
    await session.commit()
    await callback.answer()


@router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    """ Все уровни квиза"""
    result = Quiz()
    if callback_data.menu_name == "main":
        await dell_user(callback, session)
    await add_user(callback, session)
    if callback_data.menu_name == "amount":
        # result.season = str(callback_data.page).split('_')[1]
        print("=" * 50)
        print(result)
        print("=" * 50)
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "place":
        result.amount = str(callback_data.page).split('_')[1]
        print("=" * 50)
        print(result)
        print("=" * 50)
    elif callback_data.menu_name == "style":
        result.place = str(callback_data.page).split('_')[1]
        print("=" * 50)
        print(result)
        print("=" * 50)
    elif callback_data.menu_name == "colors":
        result.style = str(callback_data.page).split('_')[1]
        print("=" * 50)
        print(result)
        print("=" * 50)
    elif callback_data.menu_name == "fashion":
        result.colors = str(callback_data.page).split('_')[1]
        print("=" * 50)
        print(result)
        print("=" * 50)
    elif callback_data.menu_name == "costume":
        result.fashion = str(callback_data.page).split('_')[1]
        print("=" * 50)
        print(result)
        print("=" * 50)
    elif callback_data.menu_name == "main":
        result.costume = str(callback_data.page).split('_')[1]
        print("=" * 50)
        print(result)
        print("=" * 50)
    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )
    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()
