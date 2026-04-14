import uvicorn
from fastapi import FastAPI
from contextlib import asynccontextmanager

from database import create_tables, delete_tables
from router import router as tasks_router

@asynccontextmanager # очищение базы при включении для удобства
async def lifespan(app: FastAPI):
    await delete_tables()
    print('База очищена')
    await create_tables()
    print('база готова к работе')
    yield
    print('выключение')


app = FastAPI(lifespan=lifespan)
app.include_router(tasks_router)


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)