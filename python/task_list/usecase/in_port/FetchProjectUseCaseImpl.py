from task_list.usecase.in_port.Input import Input
from task_list.usecase.in_port.FetchProjectInput import FetchProjectInput
from task_list.usecase.ProjectDto import ProjectDto

class FetchProjectUseCaseImpl(FetchProjectInput, Input):

    _project : ProjectDto

    def setProject(self, project:ProjectDto):
        self._project = project

    def getProject(self) -> ProjectDto:
        return self._project