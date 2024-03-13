from task_list.usecase.in_port.Input import Input
from task_list.usecase.in_port.FetchCmdInput import FetchCmdInput

class FetchCmdUseCaseImp(FetchCmdInput, Input):

    _command : str

    def setCmd(self, cmd:str):
        self._command = cmd

    def getCmd(self) -> str:
        return self._command