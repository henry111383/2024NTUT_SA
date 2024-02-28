from typing import Dict, List
from task_list.console import Console
from task_list.task import Task

class TaskList:
    def __init__(self) -> None:
        self.last_id: int = 0
        self.tasks: Dict[str, List[Task]] = dict()