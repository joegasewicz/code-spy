# Code Spy
Watches for file changes & runs tasks against your Python code.


### Install
```bash
 pip install code-spy
```

### Quickstart

```python
from flask import Flask
from code_spy import (
    CodeSpy,
    MyPyTask,
    DevServerTask,
    PylintTask,
    PytestTask,
)


if __name__ == "__main__":
    
    # Create an instance of a WSGI application
    flask = Flask(__name__)
    
    # Pass the code spy shipped tasks to the `tasks` kwarg:
    cs = CodeSpy(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            PylintTask(path="routes", rcfile=".pylintrc"),
            PytestTask(path="tests"),
            DevServerTask(wsgi_app=flask),
        ]
    )
    
    # Now call `watch`, that's it!
    cs.watch()
```

### Tasks
- **Mypy** ✅
- **SimpleHttpServer** ✅
- **Pylint** ✅
- **Pytest** ✅
 
### Tasks Requiring Library Installs
To restrict the amount of third party libraries that ship with code-spy, the rest of the tasks
require library installs:

- **ISort** *TODO*
- **Flake8** *TODO*
- **Bandit** *TODO*
- **Sphinx** *TODO*
- **Custom Task** *TODO*
