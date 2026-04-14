from pydantic import BaseModel


class STaskAdd(BaseModel): #создаёт классы с жёсткой валидацией данных
    name: str
    description: str | None = None

class STask(STaskAdd):
    id: int


class STaskId(BaseModel):
    ok: bool = True
    task_id: int