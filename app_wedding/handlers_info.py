from aiogram import F, Router
from aiogram.types import CallbackQuery, Message
import app_wedding.keyboards as kb
from app_wedding.database.db import db_quiz

router_eight = Router()


@router_eight.callback_query(F.data == 'costume')
async def back_fashion(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Вернулись в выбор костюмов', reply_markup=kb.costume)


@router_eight.callback_query(F.data == 'menu')
async def next_costume(callback: CallbackQuery):
    await callback.answer()
    await callback.message.edit_text(
        'Меню', reply_markup=kb.main)
