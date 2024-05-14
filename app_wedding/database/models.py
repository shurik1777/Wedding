from sqlalchemy import DateTime, String, BigInteger, func, Text, ForeignKey, Column, Numeric
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column, relationship


class Base(DeclarativeBase):
    created: Mapped[DateTime] = mapped_column(DateTime, default=func.now())
    updated: Mapped[DateTime] = mapped_column(DateTime, default=func.now(), onupdate=func.now())


class Quiz(Base):
    """ Наполнение результирующего словаря """
    __tablename__ = 'quiz'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id = Column(Numeric, ForeignKey('user.id'), index=True)
    season: Mapped[str] = mapped_column(String(25))
    amount: Mapped[str] = mapped_column(String(25))
    place: Mapped[str] = mapped_column(String(25))
    style: Mapped[str] = mapped_column(String(25))
    colors: Mapped[str] = mapped_column(String(25))
    fashion: Mapped[str] = mapped_column(String(25))
    costume: Mapped[str] = mapped_column(String(25))
    #
    # def __str__(self):
    #     return f'{self.season} {self.amount} {self.place} {self.style} {self.colors} {self.fashion} {self.costume}'


class Banner(Base):
    __tablename__ = 'banner'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    name: Mapped[str] = mapped_column(String(15), unique=True)
    image: Mapped[str] = mapped_column(String(150), nullable=True)
    description: Mapped[str] = mapped_column(Text, nullable=True)


class User(Base):
    __tablename__ = 'user'

    id: Mapped[int] = mapped_column(primary_key=True, autoincrement=True)
    user_id: Mapped[int] = mapped_column(Numeric, unique=True)

    quizzes = relationship("Quiz", backref="user")
