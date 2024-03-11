from task_list.service.AbsractParser import AbstractParser

from task_list.service.implement.commandScanner import CommandScanner
from task_list.service.implement.commandBuilder import CommandBuilder

class CommandParser(AbstractParser):
    def __init__(self):#, scanner:CommandScanner, builder:CommandBuilder):
        self.__scanner = CommandScanner()
        self.__builder = CommandBuilder()

    def setInput(self, input:str):
        self.__scanner.setInput(input)

    def Parse(self):
        cmdName = self.__scanner.nextToken()
        if cmdName == "show":
            self.__builder.buildShowCommand()
        elif cmdName == "add":
            cmdName = self.__scanner.nextToken()
            if cmdName == "project":
                args = self.__scanner.getAllToken()
                self.__builder.buildAddProjectCommand(args)
            elif cmdName == "task":
                projectName = self.__scanner.nextToken()
                taskDct = self.__scanner.getAllToken()
                self.__builder.buildAddTaskCommand(projectName, taskDct)
            else :
                self.__builder.buildErrorCommand(cmdName) # error
        elif cmdName == "check":
            args = self.__scanner.nextToken()
            self.__builder.buildCheckCommand(args)
        elif cmdName == "uncheck":
            args = self.__scanner.nextToken()
            self.__builder.buildUncheckCommand(args)
        # elif cmdName == "help":
        #     self.__builder.buildHelpCommand()
        elif cmdName == "deadline":
            taskID = self.__scanner.nextToken()
            deadline = self.__scanner.nextToken()
            self.__builder.buildDeadlineCommand(taskID, deadline)
        else :
            self.__builder.buildErrorCommand(cmdName) # error

    def getCommand(self):
        return self.__builder.getCommand()
    
    
    
