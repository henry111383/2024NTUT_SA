class Task:
    def __init__(self, id_:str, projectID:int, description:str, done:bool) -> None:
        self._projectID = projectID
        self._id : str = id_
        self._description = description
        self._isDone : bool = done

    @property
    def id(self) -> str:
        return self._id
    
    @property
    def projectID(self) -> int:
        return self._projectID

    @property
    def description(self):
        return self._description

    @property
    def isDone(self) -> bool:
        return self._isDone
    
    @isDone.setter
    def isDone(self, done: bool):
        self._isDone = done

    

