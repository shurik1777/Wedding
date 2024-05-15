from typing import Dict

from aiogram import Router, types
from aiogram.filters import CommandStart
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy.orm import load_only

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


# async def get_quiz_dict(session: AsyncSession, user_id: int) -> Dict[str, str]:
#     async with session() as s:
#         quiz_instance = await s.query(Quiz).filter(Quiz.user_id == user_id).first()
#         if quiz_instance:
#             return quiz_instance.to_dict()

# # Usage example
#     result_dict = await get_quiz_dict(session, user_id)
#     print(result_dict)
async def get_quiz_values(session: AsyncSession, user_id: int) -> dict:
    from sqlalchemy import select

    # Создаем запрос, чтобы выбрать все строки из таблицы Quiz, где user_id равен указанному значению
    stmt = select(Quiz).where(Quiz.user_id == user_id)

    # Отправляем запрос к БД
    result = await session.execute(stmt)

    # Инициализируем словарь, в котором будем хранить результаты
    quiz_values = {}

    # Обрабатываем каждую строку результата
    for row in result.scalars():
        # Преобразуем объект строки в словарь
        row_dict = row.__dict__
        # Исключаем из словаря внутренние атрибуты объекта строки
        row_dict.pop('_sa_instance_state', None)
        # Добавляем словарь в результирующий словарь
        quiz_values = row_dict

    return quiz_values

@router.callback_query(EndMenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: EndMenuCallBack, session: AsyncSession):
    """ Результирующий хендлер """
    if callback_data.menu_name == "end":
        # quizzes = {(q.id, q.user_id, q.season, q.amount, q.place, q.style, q.colors, q.fashion, q.costume) for q in
        #            session.query(Quiz).options(load_only(*Quiz.__table__.columns.keys())).fetch()}
        print("=" * 50)
        result = await get_quiz_values(session, user_id=callback.from_user.id)
        print(result)
    await callback.answer()
