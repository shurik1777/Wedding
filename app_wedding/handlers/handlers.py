from aiogram import F, Router, types
from aiogram.filters import CommandStart
from aiogram.types import CallbackQuery
from app_wedding.database.db import db_quiz
from sqlalchemy.ext.asyncio import AsyncSession

from aiogram.utils.formatting import Bold

import app_wedding.handlers_old.keyboards as kb
from app_wedding.filters.chat_types import ChatTypeFilter
from app_wedding.kbds.inline import MenuCallBack, SeasonCallBack
from app_wedding.menu_processing import get_menu_content

router = Router()
router.message.filter(ChatTypeFilter(["private"]))


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


@router.callback_query(SeasonCallBack.filter())
async def season_menu(callback: types.CallbackQuery, callback_data: SeasonCallBack, session: AsyncSession):
    """ 1 уровень квиза"""
    media, reply_markup = await get_menu_content(
        session,
        level=callback_data.level,
        menu_name=callback_data.menu_name,
    )

    await callback.message.edit_media(media=media, reply_markup=reply_markup)
    await callback.answer()


@router.callback_query(F.data == 'quiz')
async def season_quiz(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        Bold('Выбор сезона').as_html(), reply_markup=kb.main)
    db_quiz.clear()
    db_quiz['user_id'] = callback.message.from_user.id


# @router.message(F.photo)
# async def get_photo(message: Message):
#     await message.answer(f'ID фото: {message.photo[-1].file_id}')


""" 0й Уровень """


@router.callback_query(F.data == 'about')
async def main_about(callback: CallbackQuery):
    await callback.answer('Вы выбрали "О нас"')
    await callback.message.edit_text(
        'Супер команда специалистов из ГБ', reply_markup=kb.back)


@router.callback_query(F.data == 'about_b')
async def main_about_b(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Бот помогает устроить вашу свадьбу', reply_markup=kb.back)


@router.callback_query(F.data.startswith('Назад'))
async def back_main(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'И снова привет', reply_markup=kb.main)
