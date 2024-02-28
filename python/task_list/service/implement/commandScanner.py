from task_list.service.AbstractScanner import AbstractScanner

class CommandScanner(AbstractScanner):
    def __init__(self) -> None:
        super().__init__()
        self.__token = None

    def setInput(self, input: str):
        self.__input = input
        self.__tokenList = self.__input.split(" ")
        # print("now input is ", self.__tokenList)

    def nextToken(self):
        if self.isDone():
            self.token = None
        self.__token = self.__tokenList.pop(0)
        # print("token:", self.__token)
        # print("List剩下:", self.__tokenList)
        return self.__token

    def getAllToken(self):
        # print("args:", " ".join(self.__tokenList))
        return " ".join(self.__tokenList)
    
    def isDone(self):
        return len(self.__tokenList) == 0