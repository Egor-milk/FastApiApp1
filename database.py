from typing import Optional

from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column


engine = create_async_engine(
    'sqlite+aiosqlite:///task.db'#url базы данных название бд+ драйвер
)                     #///название файлика

new_session = async_sessionmaker(engine, expire_on_commit=False)
#expire_on_commit=False Сохраняет данные в объекте после commit.

class Model(DeclarativeBase):
    pass


class TasksOrm(Model): #orm = table
    __tablename__ = 'tasks'

    # Mapped[int] говорит Python, что это целое число
    # mapped_column() отвечает за настройки в самой БД
    id: Mapped[int] = mapped_column(primary_key=True)
    name: Mapped[str]
    description: Mapped[Optional[str]]

# функция для создания таблиц
async def create_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.create_all)



#функция для удаления таблиц
async def delete_tables():
    async with engine.begin() as conn:
        await conn.run_sync(Model.metadata.drop_all)