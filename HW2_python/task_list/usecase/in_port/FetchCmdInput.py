from abc import ABC, abstractmethod

class FetchCmdInput(ABC):

    _command : str

    @abstractmethod
    def setCmd(self, cmd:str):
        pass

    @abstractmethod
    def getCmd(self) -> str:
        pass