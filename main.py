from typing import Annotated

import uvicorn
from fastapi import FastAPI, Depends
from pydantic import BaseModel

from contextlib import asynccontextmanager

from database import create_tables, delete_tables


@asynccontextmanager # очищение базы при включении для удобства
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('база готова к работе')
    yield
    print('выключение')


app = FastAPI(lifespan=lifespan)

class STaskAdd(BaseModel): #создаёт классы с жёсткой валидацией данных
    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int

tasks = []
@app.post('/tasks')
async def add_task(
        task: Annotated[STaskAdd, Depends()] #depends при передаче
        # в него pydantic модели (речь про STaskAdd) воспринимает поля name и discription
        # как Query-параметры
):
    tasks.append(task)
    return {'ok': True}

# @app.get('/tasks')
# def get_tasks():
#     task = Task(name='Запиши это видео')
#     return {'data': task}




if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)