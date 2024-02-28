import sys

from task_list.console import Console
from task_list.app import App
from task_list.task_list import TaskList

from task_list.service.implement.command import *


def main():
    # command_list = [showCommand(), addProjectCommand(), addTaskCommand(), checkCommand(), uncheckCommand()]
    
    App(taskList=TaskList(), console=Console(sys.stdin, sys.stdout)).run()
    # task_list = TaskList(Console(sys.stdin, sys.stdout))
    # task_list.setCommandList(command_list)
    # task_list.run()


if __name__ == "__main__":
    main()

