from abc import ABC, abstractmethod

class FetchShowOutput(ABC):

    _info : str

    @abstractmethod
    def setString(self, info:str):
        pass

    @abstractmethod
    def getString(self) -> str:
        pass