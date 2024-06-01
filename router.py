from fastapi import APIRouter
from schemas import STaskAdd, STask, STaskId
from typing_extensions import Annotated
from typing import List
from fastapi import Depends
from repository import TaskRepository



router = APIRouter(
    prefix="/tasks",
    tags=["tasks"],
)


@router.get("") 
async def get_tasks() -> List[STask]:
    tasks = await TaskRepository.find_all()
    return {"data": tasks}


@router.post("") 
async def add_task(task: Annotated[STaskAdd, Depends()])-> STaskId:
    task_id = await TaskRepository.add_one(task)
    return {"ok": True}