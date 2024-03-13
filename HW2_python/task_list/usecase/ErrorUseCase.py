from task_list.usecase.in_port.FetchCmdUseCaseImp import FetchCmdUseCaseImp
from task_list.usecase.out_port.FetchShowOutput import FetchShowOutput

class ErrorUseCase():

    @staticmethod
    def execute(input:FetchCmdUseCaseImp, output:FetchShowOutput):
        cmd = input.getCmd()
        output.setString(cmd)
        