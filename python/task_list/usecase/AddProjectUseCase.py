from task_list.entity.Project import Project
from task_list.usecase.ProjectMapper import ProjectMapper
from task_list.usecase.in_port.FetchCmdUseCaseImp import FetchCmdUseCaseImp
from task_list.usecase.out_port.FetchProjectOutput import FetchProjectOutput

from task_list.usecase.Command import Command
class AddProjectUseCase(Command):
    """add project <project name>"""

    @staticmethod
    def execute(input:FetchCmdUseCaseImp):
        map = ProjectMapper()
        projectName = input.getCmd()
        map.add(Project(map.length(), projectName))

