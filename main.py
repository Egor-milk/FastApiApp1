import uvicorn
from fastapi import FastAPI
from pydantic import BaseModel


app = FastAPI()

class Task(BaseModel): #создаёт классы с жёсткой валидацией данных
    name: str
    description: str | None = None



@app.get('/tasks')
def get_tasks():
    task = Task(name='Запиши это видео')
    return {'data': task}


if __name__ == '__main__':
    uvicorn.run('main:app', host='localhost', port=8000, reload=True)