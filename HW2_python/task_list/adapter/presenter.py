from abc import ABC, abstractclassmethod

class Presenter:
    @abstractclassmethod
    def print(self, string, end, flush) -> None:
        pass

    def input(self, prompt) -> str:
        pass
    