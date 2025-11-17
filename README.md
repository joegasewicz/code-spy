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
)


if __name__ == "__main__":
    
    # Create an instance of a WSGI application
    flask = Flask(__name__)
    
    # Pass the code spy shipped tasks to the `tasks` kwarg:
    cs = CodeSpy(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            DevServerTask(wsgi_app=flask),
            PylintTask(path="routes", rcfile=".pylintrc"),
        ]
    )
    
    # Now call `watch`, that's it!
    cs.watch()
```

### Tasks
- **Mypy** ✅
- **SimpleHttpServer** ✅
- **Pylint** ✅
- **Pytest** *TODO*
 
### Plugins 
- **ISort** *TODO*
- **Flake8** *TODO*
- **Bandit** *TODO*
- **Sphinx** *TODO*
- **Custom Task** *TODO*
