from abc import ABC, abstractmethod
from task_list.usecase.ProjectDto import ProjectDto

class FetchProjectOutput(ABC):

    _project : ProjectDto

    @abstractmethod
    def setProject(self, project:ProjectDto):
        pass

    @abstractmethod
    def getProject(self) -> ProjectDto:
        pass