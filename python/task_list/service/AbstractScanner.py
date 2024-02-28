
class AbstractScanner:
    def __init__(self) -> None:
        pass

    def setInput(self, input: str):
        # virtual
        raise NotImplementedError("Virtual function")

    def nextToken(self):
        # virtual
        raise NotImplementedError("Virtual function")
    
