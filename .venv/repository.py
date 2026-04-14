from database import new_session, TasksOrm
from sqlalchemy import select

class TaskRepository:
    @classmethod
    async def add_one(cls, data: STaskAdd) -> int:
        async with new_session() as session:
            task_dict = task.model_dump()

            task = TasksOrm(**task_dict)
            session.add(task)
            await session.flush() #синхронизирует состояние объектов
            # в памяти с базой данных, но не завершает транзакцию окончательно.
            await session.commit() #все изменения
            # добавленные через add закоммитятся в базу данных
            # во время await session.commit()
            return task.id


    @classmethod
    async def find_all(cls):
        async with new_session() as session:
            query = select(TaskOrm)
            result = await session.execute(query)
            task_models = result.scalars().all()
            # scalars() Этот метод говорит SQLAlchemy:
            # "Возьми из каждой строки только первый элемент и верни его".
            return task_models
