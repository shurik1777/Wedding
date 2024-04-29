from os import getenv
from dotenv import find_dotenv, load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine

from app_wedding.database.models import Base
from app_wedding.database.orm_query import orm_add_banner_description

from aiogram.utils.formatting import Bold, as_list, as_marked_section

load_dotenv(find_dotenv())

engine = create_async_engine(getenv("DB_URL"), echo=True)

session_maker = async_sessionmaker(bind=engine, class_=AsyncSession, expire_on_commit=False)

description_for_info_pages = {
    "main": "Добро пожаловать в свадебный бот!",
    "about_b": "Я помогу Вам придумать свадьбу мечты.",
    "about": as_list(
        as_marked_section(
            Bold("Варианты крутейших разрабов:"),
            "Юрист",
            "Инженер конструктор авиационных двигателей",
            "Просто Саня",
        ),
        sep="\n----------------------\n",
    ).as_html()
}


async def create_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)

    async with session_maker() as session:
        await orm_add_banner_description(session, description_for_info_pages)


# Возможно потребуется удаление
async def drop_db():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)
