from abc import ABC, abstractmethod
from task_list.usecase.TaskDto import TaskDto

class FetchTaskOutput(ABC):

    _task : TaskDto

    @abstractmethod
    def setTask(self, task:TaskDto):
        pass

    @abstractmethod
    def getTask(self) -> TaskDto:
        pass