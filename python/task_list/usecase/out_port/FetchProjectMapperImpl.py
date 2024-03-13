from task_list.usecase.out_port.Output import Output
from task_list.usecase.out_port.FetchProjectOutput import FetchProjectOutput
from task_list.usecase.ProjectDto import ProjectDto

class FetchProjectMapperImpl(FetchProjectOutput, Output):

    _project : ProjectDto

    def setProject(self, project:ProjectDto):
        self._project = project

    def getProject(self) -> ProjectDto:
        return self._project