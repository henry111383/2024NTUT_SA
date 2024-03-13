from abc import ABC, abstractmethod
from task_list.entity.Task import Task

class TaskMapper(ABC):
    _instance = None
    _map = dict()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(TaskMapper, cls).__new__(cls)
        return cls._instance

    def add(self, task:Task):
        self._map[task.id] = task

    def find(self, id:int)->Task:
        if self._map[id] :
            return self._map[id]
        else:
            pass

    def findByProjectID(self, id:int):
        tasks = []
        for key in self._map:
            if self._map[key].projectID == id:
                tasks.append(self._map[key])
        return tasks

    def length(self):
        return len(self._map)
    
    @property
    def map(self):
        return self._map