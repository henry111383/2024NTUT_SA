from task_list.usecase.ShowUseCase import ShowUseCase
from task_list.usecase.AddProjectUseCase import AddProjectUseCase
from task_list.usecase.AddTaskUseCase import AddTaskUseCase
from task_list.usecase.CheckUseCase import CheckUseCase
from task_list.usecase.UncheckUseCase import UncheckUseCase
from task_list.usecase.ErrorUseCase import ErrorUseCase


from task_list.usecase.in_port.FetchCmdUseCaseImp import FetchCmdUseCaseImp
from task_list.usecase.in_port.FetchProjectUseCaseImpl import FetchProjectUseCaseImpl
from task_list.usecase.in_port.FetchTaskUseCaseImpl import FetchTaskUseCaseImpl
from task_list.usecase.out_port.FetchShowPresenterImpl import FetchShowPresenterImpl

from task_list.adapter.presenter import Presenter
from task_list.adapter.console import Console
from task_list.usecase.Command import Command



class Controller:
    QUIT = "quit"

    def __init__(self, presenter:Presenter) -> None:
        self._presenter = presenter
        self._injector = FetchCmdUseCaseImp()
        self._getter = FetchShowPresenterImpl()

    def run(self) -> None:
        while True:
            original_cmd = self._presenter.input("> ")
            self._injector.setCmd(original_cmd)
            command = original_cmd.split(" ",1)
            if command[0] == self.QUIT:
                break
            if command[0] == 'help':
                self.showCommand()
                continue
            if command[0] == 'add':
                cmd = command[1].split(" ",1)
                self._injector.setCmd(cmd[1])
                if cmd[0] == 'task':
                    AddTaskUseCase.execute(self._injector)
                    continue
                if cmd[0] == 'project':
                    AddProjectUseCase.execute(self._injector)
                    continue
            if command[0] == 'show':
                ShowUseCase.execute(self._getter)
                self._presenter.print(self._getter.getString())
                continue
            if command[0] == 'check':
                cmd = command[1].split(" ",1)
                self._injector.setCmd(cmd[0])
                CheckUseCase.execute(self._injector)
                continue
            if command[0] == 'uncheck':
                cmd = command[1].split(" ",1)
                self._injector.setCmd(cmd[0])
                UncheckUseCase.execute(self._injector)
                continue

            self._injector.setCmd(original_cmd)
            ErrorUseCase.execute(self._injector, self._getter)
            self._presenter.print(f"I don't know what the command {self._getter.getString()} is.")
            continue


    def showCommand(self):
        self._presenter.print("Commands:")
        child_classes = Command.__subclasses__()
        for child_class in child_classes:
            self._presenter.print("  " + child_class.__doc__)