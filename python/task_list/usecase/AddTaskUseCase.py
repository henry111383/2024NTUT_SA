from task_list.entity.Task import Task
from task_list.usecase.TaskMapper import TaskMapper
from task_list.usecase.ProjectMapper import ProjectMapper
from task_list.usecase.in_port.FetchCmdUseCaseImp import FetchCmdUseCaseImp
from task_list.usecase.Command import Command

class AddTaskUseCase(Command):
    """add task <project name> <task description>"""
    @staticmethod
    def execute(input:FetchCmdUseCaseImp):
        task_map = TaskMapper()
        project_map = ProjectMapper()

        name = input.getCmd().split(" ", 1)
        task_map.add(Task(task_map.length()+1, project_map.findByName(name[0]), name[1], False))

