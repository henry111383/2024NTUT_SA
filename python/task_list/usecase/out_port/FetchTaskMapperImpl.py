from task_list.usecase.out_port.Output import Output
from task_list.usecase.out_port.FetchTaskOutput import FetchTaskOutput
from task_list.usecase.TaskDto import TaskDto

class FetchTaskMapperImpl(FetchTaskOutput, Output):

    _task : TaskDto

    def setTask(self, task:TaskDto):
        self._task = task

    def getTask(self) -> TaskDto:
        return self._task