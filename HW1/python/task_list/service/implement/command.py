from task_list.service.AbstractCommand import Command
from task_list.console import Console
from task_list.task import Task
from datetime import datetime, date

# Implement

# show
class showCommand(Command):
    """show"""
    def __init__(self, name: str="show", instructment: str="show") -> None:
        super().__init__(name, instructment)

    def process(self, target, console:Console):
        for project, tasks in target.tasks.items():
            console.print(project)
            for task in tasks:
                output_str = f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}"
                deadline = task.getDeadline()
                if deadline:
                    output_str += f" (deadline:{deadline})"
                console.print(output_str)
                # console.print(f"{task.id}")
            console.print()
    
# add project 
class addProjectCommand(Command):
    """add project <project name>"""
    def __init__(self, name: str="add project", instructment: str="add project <project name>") -> None:
        super().__init__(name, instructment)

    def setProjectName(self, projectName: str):
        self.__projectName = projectName

    def process(self, target, console:Console):
        target.tasks[self.__projectName] = []

# add task
class addTaskCommand(Command):
    """add task <project name> <task description>"""
    def __init__(self, name: str="add task", instructment: str="add task <project name> <task description>") -> None:
        super().__init__(name, instructment)

    def setTaskDescription(self, projectName: str, taskDct: str):
        self.__projectName = projectName
        self.__taskDct = taskDct

    def process(self, target, console:Console):

        def next_id() -> str:
            target.last_id += 1
            return str(target.last_id)
        
        project_tasks = target.tasks.get(self.__projectName)
        if project_tasks is None:
            console.print(f"Could not find a project with the name {self.__projectName}.")
            console.print()
            return
        project_tasks.append(Task(next_id(), self.__taskDct, False))
        
# check
class checkCommand(Command):
    """check <task ID>"""
    def __init__(self, name: str="check", instructment: str="check <task ID>") -> None:
        super().__init__(name, instructment)

    def setTaskID(self, taskID: str):
        self.__taskID:str = taskID

    def process(self, target, console:Console):
        set_done(self.__taskID, True, target, console)

# uncheck
class uncheckCommand(Command):
    """uncheck <task ID>"""
    def __init__(self, name: str="uncheck", instructment: str="uncheck <task ID>") -> None:
        super().__init__(name, instructment)

    def setTaskID(self, taskID: str):
        self.__taskID:str = taskID
    
    def process(self, target, console:Console):
        set_done(self.__taskID, False, target, console)


def set_done(id_string: str, done: bool, target, console) -> None:
        id_ = str(id_string)
        for project, tasks in target.tasks.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    return
        console.print(f"Could not find a task with an ID of {id_}")
        console.print()

# Error
class errorCommand(Command):
    """error"""
    def __init__(self, name: str="error", instructment: str="error") -> None:
        super().__init__(name, instructment)

    def setMsg(self, msg:str):
        self.__msg = msg

    def process(self, target, console):
        console.print(f"I don't know what the command {self.__msg} is.")
        console.print()

# feature 1
class deadlineCommnad(Command):
    """deadline <ID> <date>"""
    def __init__(self, name: str="deadline", instructment: str="deadline <ID> <date>") -> None:
        super().__init__(name, instructment)

    def setID(self, id_:str, date_:str):
        self.__id = id_
        self.__date = date_

    def process(self, target, console:Console):
        for project, tasks in target.tasks.items():
            for index, task in enumerate(tasks):
                if task.getId() == self.__id:
                    target.tasks[project][index].setDeadline(self.__date)
                    