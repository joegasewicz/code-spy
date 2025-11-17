# Code Spy
Watches for file changes & runs tasks against your Python code.


### Install
```bash
 pip install code-spy
```

### Quickstart

```python
from flask import Flask
from code_spy import CodeSpy, MyPyTask, DevServerTask

if __name__ == "__main__":
    flask = Flask(__name__)
    cs = CodeSpy(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            DevServerTask(wsgi_app=flask),
        ]
    )
    cs.watch()
```

### Tasks
- **Mypy** ✅
- **SimpleHttpServer** ✅
- **Pylint** ✅
- **Pytest** *TODO*
- **ISort** *TODO*
- **Flake8** *TODO*
- **Bandit** *TODO*
- **Sphinx** *TODO*
- **Custom Task** *TODO*


