from typing import Dict, List

class Project():
    def __init__(self, id:int, projectName:str) -> None:
        self._id: int = id
        self._name: str = projectName

    @property
    def id(self):
        return self._id
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, newName:str):
        self._name = newName