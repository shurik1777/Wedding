import asyncio
import logging

from aiogram.client.bot import DefaultBotProperties
from aiogram.enums import ParseMode

from os import getenv
from dotenv import find_dotenv, load_dotenv
from aiogram import Bot, Dispatcher
from app_wending.handlers import router
from app_wending.handlers_season import router_one
from app_wending.handlers_style import router_two
from app_wending.handlers_colors import router_three
from app_wending.handlers_place import router_four
from app_wending.handlers_fashion import router_five
from app_wending.handlers_amount import router_six
from app_wending.handlers_costume import router_seven
from app_wending.handlers_info import router_eight

load_dotenv(find_dotenv())


async def main():
    # bot = Bot(token=getenv('TOKEN'))

    bot = Bot(token=getenv('TOKEN'), default=DefaultBotProperties(parse_mode=ParseMode.HTML))

    dp = Dispatcher()
    dp.include_router(router)
    dp.include_router(router_one)
    dp.include_router(router_two)
    dp.include_router(router_three)
    dp.include_router(router_four)
    dp.include_router(router_five)
    dp.include_router(router_six)
    dp.include_router(router_seven)
    dp.include_router(router_eight)
    await dp.start_polling(bot)


if __name__ == '__main__':
    # logging.basicConfig(level=logging.INFO)
    try:
        print('Я запустился')
        asyncio.run(main())
    except KeyboardInterrupt:
        print('Exit')
