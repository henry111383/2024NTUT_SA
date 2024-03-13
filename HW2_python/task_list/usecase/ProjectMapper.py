from abc import ABC, abstractmethod
from task_list.entity.Project import Project

class ProjectMapper(ABC):
    _instance = None
    _map = dict()

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super(ProjectMapper, cls).__new__(cls)
        return cls._instance

    def add(self, project:Project):
        self._map[project.id] = project

    def find(self, id:int)->Project:
        if self._map[id] :
            return self._map[id]
        else:
            pass

    def findByName(self, name:str) -> int:
        for key in self._map:
            if self._map[key].name == name:
                return int(key)

    def length(self):
        return len(self._map)
    
    @property
    def map(self):
        return self._map