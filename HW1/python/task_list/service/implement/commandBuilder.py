from task_list.service.AbstractBuilder import AbstractBuilder

from task_list.service.implement.command import *

class CommandBuilder(AbstractBuilder):
    def __init__(self) -> None:
        super().__init__()

    def buildShowCommand(self):
        self.__cmd = showCommand()

    def buildAddProjectCommand(self, projectName: str):
        self.__cmd = addProjectCommand()
        self.__cmd.setProjectName(projectName)

    def buildAddTaskCommand(self, projectName:str, taskDct: str):
        self.__cmd = addTaskCommand()
        self.__cmd.setTaskDescription(projectName, taskDct)
    
    def buildCheckCommand(self, taskID: str):
        self.__cmd = checkCommand()
        self.__cmd.setTaskID(taskID)

    def buildUncheckCommand(self, taskID: str):
        self.__cmd = uncheckCommand()
        self.__cmd.setTaskID(taskID)
    
    def buildHelpCommand(self):
        self.__cmd = helpCommand()

    def buildErrorCommand(self, msg):
        self.__cmd = errorCommand()
        self.__cmd.setMsg(msg)
    
    def getCommand(self):
        return self.__cmd