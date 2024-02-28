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

## How did i do ?
- Implemented task list functionality using the Strategy pattern.
- Segregated methods from the tasklist for better organization.
- Improved extensibility by adopting design patterns like Builder, Scanner, and Parser.
- Subclassed abstract class Command to enhance extensibility further.
- Facilitated flexibility in adding new commands and functionalities.
- Extracted irrelevant attributes from TaskList, such as the running program being class "App".
- Ensured each class has a single responsibility for better code organization.
- Enhanced cohesion and clarity of each class's purpose.
Contributed to a more robust and understandable design.
