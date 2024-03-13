from task_list.usecase.Command import Command
from task_list.usecase.TaskMapper import TaskMapper
from task_list.usecase.ProjectMapper import ProjectMapper
from task_list.usecase.out_port.FetchShowOutput import FetchShowOutput


class ShowUseCase(Command):
    """show"""
    
    @staticmethod
    def execute(output:FetchShowOutput):
        _task_map = TaskMapper()
        _project_map = ProjectMapper()
        output_str = ""
        for projectID in _project_map._map:
            output_str += str(_project_map._map[projectID].name)
            output_str += '\n'
            tasks = _task_map.findByProjectID(projectID)
            for task in tasks:
                output_str += f"  [{'x' if task.isDone else ' '}] {str(task.id)}: {task.description}\n"
        output.setString(output_str)

