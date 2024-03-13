HW1 refactor in Python
=====


The application requires Python 3.5 or above

To run tests:
```
cd python
python -m unittest -v
```

To run the application:
```
cd python
python -m task_list
```

```
.
├── README.md
├── setup.py
├── task_list
│   ├── __init__.py
│   ├── __main__.py
│   ├── adapter
│   │   ├── console.py
│   │   ├── controller.py
│   │   └── presenter.py
│   ├── entity
│   │   ├── Project.py
│   │   └── Task.py
│   └── usecase
│       ├── AddProjectUseCase.py
│       ├── AddTaskUseCase.py
│       ├── CheckUseCase.py
│       ├── Command.py
│       ├── ErrorUseCase.py
│       ├── ProjectDto.py
│       ├── ProjectMapper.py
│       ├── ShowUseCase.py
│       ├── TaskDto.py
│       ├── TaskMapper.py
│       ├── UncheckUseCase.py
│       ├── in_port
│       │   ├── FetchCmdInput.py
│       │   ├── FetchCmdUseCaseImp.py
│       │   ├── FetchProjectInput.py
│       │   ├── FetchProjectUseCaseImpl.py
│       │   ├── FetchTaskInput.py
│       │   ├── FetchTaskUseCaseImpl.py
│       │   └── Input.py
│       └── out_port
│           ├── FetchProjectMapperImpl.py
│           ├── FetchProjectOutput.py
│           ├── FetchShowOutput.py
│           ├── FetchShowPresenterImpl.py
│           ├── FetchTaskMapperImpl.py
│           ├── FetchTaskOutput.py
│           └── Output.py
└── tests
    ├── __init__.py
    └── test_application.py

8 directories, 36 files
```
