from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from app_wedding.database.models import Quiz
from app_wedding.database.orm_query import orm_add_user
from app_wedding.filters.chat_types import ChatTypeFilter
from app_wedding.kbds.inline import MenuCallBack, EndMenuCallBack
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
    from sqlalchemy import update
    user = callback.from_user

    update_mapping = {
        'season': ['winter', 'spring', 'summer', 'autumn'],
        'amount': ['two', 'folks', 'upto100', 'morethan100'],
        'place': ['garden', 'restaurant', 'sea', 'unique'],
        'style': ['classic', 'eccentric', 'modern', 'romantic', 'travel', 'vintage'],
        'colors': ['dirtyRose', 'emeraldGreen', 'macchiato', 'quartzPink', 'vanillaCream', 'wine'],
        'fashion': ['trapezoidal', 'naiad', 'sheath', 'ballGown', 'overalls', 'retro'],
        'costume': ['classicCostume', 'tuxedo', 'casual', 'modernCostume']
    }

    for column, possible_values in update_mapping.items():
        if values in possible_values:
            stmt = update(Quiz).where(user.id == Quiz.user_id).values(**{column: values})
            await session.execute(stmt)
            break

    await session.commit()
    await callback.answer()

# async def add_values(callback: types.CallbackQuery, session: AsyncSession, values: str):
#     user = callback.from_user
#     from sqlalchemy import update
#     if values in ['winter', 'spring', 'summer', 'autumn']:
#         stmt = update(Quiz).where(user.id == Quiz.user_id).values(
#             season=values)
#         await session.execute(stmt)
#     elif values in ['two', 'folks', 'upto100', 'morethan100']:
#         stmt = update(Quiz).where(user.id == Quiz.user_id).values(
#             amount=values)
#         await session.execute(stmt)
#     elif values in ['garden', 'restaurant', 'sea', 'unique']:
#         stmt = update(Quiz).where(user.id == Quiz.user_id).values(
#             place=values)
#         await session.execute(stmt)
#     elif values in ['classic', 'eccentric', 'modern', 'romantic', 'travel', 'vintage']:
#         stmt = update(Quiz).where(user.id == Quiz.user_id).values(
#             style=values)
#         await session.execute(stmt)
#     elif values in ['dirtyRose', 'emeraldGreen', 'macchiato', 'quartzPink', 'vanillaCream', 'wine']:
#         stmt = update(Quiz).where(user.id == Quiz.user_id).values(
#             colors=values)
#         await session.execute(stmt)
#     elif values in ['trapezoidal', 'naiad', 'sheath', 'ballGown', 'overalls', 'retro']:
#         stmt = update(Quiz).where(user.id == Quiz.user_id).values(
#             fashion=values)
#         await session.execute(stmt)
#     elif values in ['classicCostume', 'tuxedo', 'casual', 'modernCostume']:
#         stmt = update(Quiz).where(user.id == Quiz.user_id).values(
#             costume=values)
#         await session.execute(stmt)
#     await session.commit()
#     await callback.answer()


@router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    """ Все уровни квиза"""
    if callback_data.menu_name == "main":
        await dell_user(callback, session)
    await add_user(callback, session)
    if callback_data.menu_name == "amount":
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "place":
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "style":
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "colors":
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "fashion":
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "costume":
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    elif callback_data.menu_name == "end":
        await add_values(callback, session, values=str(callback_data.page).split('_')[1])
    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )
    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()

@router.callback_query(EndMenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: EndMenuCallBack, session: AsyncSession):
    """ Результирующий хендлер """
    if callback_data.menu_name == "end":
        print('Поймал end')
    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )
    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()