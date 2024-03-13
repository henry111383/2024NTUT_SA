from abc import ABC, abstractmethod
from task_list.usecase.ProjectDto import ProjectDto

class FetchProjectInput(ABC):

    _project : ProjectDto

    @abstractmethod
    def setProject(self, project:ProjectDto):
        pass

    @abstractmethod
    def getProject(self) -> ProjectDto:
        pass