import asyncio
import logging

from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from os import getenv
from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher

from app_wedding.middlewares.db import DataBaseSession

from app_wedding.database.engine import session_maker, drop_db, create_db
from app_wedding.handlers import router
from app_wedding.handlers_season import router_one
from app_wedding.handlers_style import router_two
from app_wedding.handlers_colors import router_three
from app_wedding.handlers_place import router_four
from app_wedding.handlers_fashion import router_five
from app_wedding.handlers_amount import router_six
from app_wedding.handlers_costume import router_seven
from app_wedding.handlers_info import router_eight

load_dotenv(find_dotenv())

from app_wedding.user_group import user_group_router
from app_wedding.admin_private import admin_router

bot = Bot(token=getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
bot.my_admins_list = []


async def on_startup(bot):
    # run_param = False
    # if run_param:
    #     await drop_db()

    await create_db()


async def main():
    dp = Dispatcher()

    dp.startup.register(on_startup)

    dp.update.middleware(DataBaseSession(session_pool=session_maker))

    dp.include_router(router)
    dp.include_router(router_one)
    dp.include_router(router_two)
    dp.include_router(router_three)
    dp.include_router(router_four)
    dp.include_router(router_five)
    dp.include_router(router_six)
    dp.include_router(router_seven)
    dp.include_router(router_eight)
    dp.include_router(user_group_router)
    dp.include_router(admin_router)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    try:
        print('Я запустился')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
