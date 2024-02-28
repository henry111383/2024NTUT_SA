from typing import Dict, List

# from task_list.console import Console
# from task_list.task import Task

from task_list.task_list import TaskList
from task_list.service.AbstractCommand import Command
from task_list.service.implement.commandParser import CommandParser

class App:
    QUIT = "quit"

    def __init__(self, taskList:TaskList, console) -> None:
        self.__taskList = taskList
        self.__console = console
        self.__commandParser = CommandParser()
    
    def setTaskList(self, taskList):
        self.__taskList = taskList
    
    def getTaskList(self):
        return self.__taskList
    
    def setConsole(self, console):
        self.__console = console

    def getConsole(self):
        return self.__console
    
    def run(self) -> None:
        while True:
            command = self.__console.input("> ")
            if command == self.QUIT:
                break
            if command == 'help':
                self.showCommand()
                continue
            self.__commandParser.setInput(command)
            self.__commandParser.Parse()
            cmd = self.__commandParser.getCommand()
            cmd.process(target=self.__taskList, console=self.__console)

    def showCommand(self):
        self.__console.print("Commands:")
        child_classes = Command.__subclasses__()
        for child_class in child_classes:
            if child_class.__name__ != "errorCommand":
                self.__console.print("  " + child_class.__doc__)