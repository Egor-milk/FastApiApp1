from typing import Annotated

from fastapi import APIRouter, Depends
from repository import TaskRepository

from schemas import STaskAdd, STask, STaskId

#APIrouter позволяет вынести ендпоинты в другой файл и удобно использовать
# их в main.py

router = APIRouter(
    prefix='/tasks',
    tags=['Таски']
)


@router.post('')
async def add_task(
        task: Annotated[STaskAdd, Depends()] #depends при передаче
        # в него pydantic модели (речь про STaskAdd) воспринимает поля name и discription
        # как Query-параметры
) -> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {'ok': True, 'task_id': task_id}

@router.get('')
async def get_tasks() -> list[STask]:
    tasks = await TaskRepository.find_all()
    return tasks