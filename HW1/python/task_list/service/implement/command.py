from task_list.service.AbstractCommand import Command
from task_list.console import Console
from task_list.task import Task
# from task_list.app import TaskList

# Implement

# show
class showCommand(Command):
    def __init__(self, name: str="show", instructment: str="show") -> None:
        super().__init__(name, instructment)

    def process(self, target, console:Console):
        for project, tasks in target.tasks.items():
            console.print(project)
            for task in tasks:
                console.print(f"  [{'x' if task.is_done() else ' '}] {task.id}: {task.description}")
            console.print()
    
# add project 
class addProjectCommand(Command):
    def __init__(self, name: str="add project", instructment: str="add project <project name>") -> None:
        super().__init__(name, instructment)

    def setProjectName(self, projectName: str):
        self.__projectName = projectName

    def process(self, target, console:Console):
        target.tasks[self.__projectName] = []

# add task
class addTaskCommand(Command):
    def __init__(self, name: str="add task", instructment: str="add task <project name> <task description>") -> None:
        super().__init__(name, instructment)

    def setTaskDescription(self, projectName: str, taskDct: str):
        self.__projectName = projectName
        self.__taskDct = taskDct

    def process(self, target, console:Console):

        def next_id() -> int:
            target.last_id += 1
            return target.last_id
        
        project_tasks = target.tasks.get(self.__projectName)
        if project_tasks is None:
            console.print(f"Could not find a project with the name {self.__projectName}.")
            console.print()
            return
        project_tasks.append(Task(next_id(), self.__taskDct, False))
        
# check
class checkCommand(Command):
    def __init__(self, name: str="check", instructment: str="check <task ID>") -> None:
        super().__init__(name, instructment)

    def setTaskID(self, taskID: str):
        self.__taskID = taskID

    def process(self, target, console:Console):
        set_done(self.__taskID, True, target, console)

# uncheck
class uncheckCommand(Command):
    def __init__(self, name: str="uncheck", instructment: str="uncheck <task ID>") -> None:
        super().__init__(name, instructment)

    def setTaskID(self, taskID: str):
        self.__taskID = taskID
    
    def process(self, target, console:Console):
        set_done(self.__taskID, False, target, console)


def set_done(id_string: str, done: bool, target, console) -> None:
        id_ = int(id_string)
        for project, tasks in target.tasks.items():
            for task in tasks:
                if task.id == id_:
                    task.set_done(done)
                    return
        console.print(f"Could not find a task with an ID of {id_}")
        console.print()

# help
class helpCommand(Command):
    def __init__(self, name: str="help", instructment: str="help") -> None:
        super().__init__(name, instructment)
        
    def process(self, target, console):
        console.print("Commands:")
        console.print("  show")
        console.print("  add project <project name>")
        console.print("  add task <project name> <task description>")
        console.print("  check <task ID>")
        console.print("  uncheck <task ID>")
        console.print()


# Error
class errorCommand(Command):
    def __init__(self, name: str="error", instructment: str="error") -> None:
        super().__init__(name, instructment)

    def setMsg(self, msg:str):
        self.__msg = msg

    def process(self, target, console):
        console.print(f"I don't know what the command {self.__msg} is.")
        console.print()

