from aiogram import Router, types
from aiogram.filters import CommandStart
# from app_wedding.database.db import db_quiz
from sqlalchemy.ext.asyncio import AsyncSession

from app_wedding.database.models import Quiz
from app_wedding.filters.chat_types import ChatTypeFilter
from app_wedding.kbds.inline import MenuCallBack, SeasonCallBack
from app_wedding.menu_processing import get_menu_content

router = Router()
router.message.filter(ChatTypeFilter(["private"]))


async def process_season_choice(season: str, user_id: int, db_quiz: dict):
    # Проверяем, есть ли уже запись для этого пользователя
    if user_id in db_quiz:
        # Обновляем существующую запись
        db_quiz[user_id][season] = True
    else:
        # Создаем новую запись для пользователя
        db_quiz[user_id] = {season: True}

    # Возвращаем обновленный словарь
    return db_quiz


async def add_data(session, db_quiz):
    # Создаем объект Quiz на основе данных из db_quiz
    data = Quiz(tg_id=db_quiz['user_id'],
                season=db_quiz['season'],
                amount=db_quiz['amount'],
                place=db_quiz['place'],
                style=db_quiz['style'],
                colors=db_quiz['colors'],
                fashion=db_quiz['fashion'],
                costume=db_quiz['costume'])
    # Добавляем объект в сессию и сохраняем изменения в БД
    async with session.begin():
        session.add(data)
        print(data)
    await session.commit()


@router.message(CommandStart())
async def start_cmd(message: types.Message, session: AsyncSession):
    media, reply_markup = await get_menu_content(session, level=0, menu_name="main")

    await message.answer_photo(media.media, caption=media.caption, reply_markup=reply_markup)


@router.callback_query(MenuCallBack.filter())
async def user_menu(callback: types.CallbackQuery, callback_data: MenuCallBack, session: AsyncSession):
    """ 0 уровень квиза"""
    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )

    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()


async def season_menu(callback: types.CallbackQuery, callback_data: SeasonCallBack, session: AsyncSession,
                      db_quiz: dict):
    """ 1 уровень квиза"""
    season = callback_data.menu_name
    user_id = callback.message.from_user.id
    # Получаем текущее состояние словаря db_quiz
    db_quiz = await process_season_choice(season, user_id, db_quiz)

    # Если это последний сезон в опросе, сохраняем данные в БД
    if all(db_quiz[user_id].values()):
        await add_data(session, db_quiz)

    # Здесь можно обновить клавиатуру или сообщение в зависимости от выбранного сезона
    # ...

    await callback.answer()
