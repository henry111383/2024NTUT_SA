from datetime import datetime, date

class Task:
    def __init__(self, id_: int, description: str, done: bool) -> None:
        self.id : str = id_
        self.description = description
        self.done : bool = done
        self.createdAt : date = date.today()
        self.deadline : date

    def getId(self):
        return self.id
    
    def getDescription(self):
        return self.description

    def setDeadline(self, deadline:date):
        self.deadline = deadline
        return self
    
    def getDeadline(self):
        return self.deadline

    def set_done(self, done: bool) -> None:
        self.done = done

    def is_done(self) -> bool:
        return self.done

