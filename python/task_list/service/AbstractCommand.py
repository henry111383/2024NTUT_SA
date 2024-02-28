
# Interface
class Command:
    def __init__(self, name: str, instructment: str) -> None:
        self.__name = name
        self.__instructment = instructment

    def process(self, target, console):
        # virtual
        raise NotImplementedError("Virtual function")
    
    def get_name(self):
        return self.__name
    
    def get_instructment(self):
        return self.__instructment
    
