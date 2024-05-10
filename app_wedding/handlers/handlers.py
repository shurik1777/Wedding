from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession

from app_wedding.database.orm_query import orm_add_user, orm_dell_user
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
    await orm_dell_user(
        session,
        user_id=user.id,
    )
    await callback.answer()


@router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    """ Все уровни квиза"""
    # print("="*50)
    # print(callback_data)
    # print("="*50)
    if callback_data.menu_name == "main":
        await dell_user(callback, session)
    await add_user(callback, session)
    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )
    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()

    # async_dict = {}
    # async_dict_var = None

    # async_dict_var.get(async_dict)
    # await add_to_async_dict(async_dict, str(callback_data.page).split('_')[0], str(callback_data.page).split('_')[1])
    # print(async_dict)
    # print("="*50)
    # print(str(callback_data.page).split('_')[0])
    # print(str(callback_data.page).split('_')[1])
    # print("=" * 50)

# async def add_data(session, db_quiz):
#     # Создаем объект Quiz на основе данных из db_quiz
#     data = Quiz(tg_id=db_quiz['user_id'],
#                 season=db_quiz['season'],
#                 amount=db_quiz['amount'],
#                 place=db_quiz['place'],
#                 style=db_quiz['style'],
#                 colors=db_quiz['colors'],
#                 fashion=db_quiz['fashion'],
#                 costume=db_quiz['costume'])
#     # Добавляем объект в сессию и сохраняем изменения в БД
#     async with session.begin():
#         session.add(data)
#         print(data)
#     await session.commit()
