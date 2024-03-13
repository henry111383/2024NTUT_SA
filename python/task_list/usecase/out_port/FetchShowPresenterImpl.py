from task_list.usecase.out_port.Output import Output
from task_list.usecase.out_port.FetchShowOutput import FetchShowOutput

class FetchShowPresenterImpl(FetchShowOutput, Output):

    _info : str

    def setString(self, info:str):
        self._info = info

    def getString(self) -> str:
        return self._info