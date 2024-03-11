from datetime import datetime, date

class Task:
    def __init__(self, id_:str, description:str, done:bool) -> None:
        self.__id : str = id_
        self.__description = description
        self.__done : bool = done
        self.__createdAt : date = date.today()
        self.__deadline : str = None

    def getId(self) -> str:
        return self.__id
    
    def getDescription(self):
        return self.__description

    def setDeadline(self, deadline:str):
        self.__deadline = deadline
        return self
    
    def getDeadline(self):
        return self.__deadline

    def set_done(self, done: bool) -> None:
        self.__done = done

    def is_done(self) -> bool:
        return self.__done

