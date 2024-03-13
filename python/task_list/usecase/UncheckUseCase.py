from task_list.entity.Task import Task
from task_list.usecase.TaskMapper import TaskMapper
from task_list.usecase.in_port.FetchCmdUseCaseImp import FetchCmdUseCaseImp
from task_list.usecase.Command import Command

class UncheckUseCase(Command):
    """uncheck <task ID>"""
    @staticmethod
    def execute(input:FetchCmdUseCaseImp):
        map = TaskMapper()


        id = input.getCmd()
        map.find(int(id)).isDone = False

