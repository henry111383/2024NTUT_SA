from task_list.usecase.in_port.Input import Input
from task_list.usecase.in_port.FetchTaskInput import FetchTaskInput
from task_list.usecase.TaskDto import TaskDto

class FetchTaskUseCaseImpl(FetchTaskInput, Input):

    _task : TaskDto

    def setTask(self, task:TaskDto):
        self._task = task

    def getTask(self) -> TaskDto:
        return self._task