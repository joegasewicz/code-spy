# Code Spy
Watches for file changes & runs tasks against your Python code.


### Install
```bash
 pip install code-spy
```

### Quickstart

```python
from flask import Flask
from dev_runner import DevRunner, MyPyTask, DevServerTask


if __name__ == "__main__":
    flask = Flask(__name__)
    dr = DevRunner(
        path=".",
        tasks=[
            MyPyTask(path="routes", mypy_file="mypy.ini"),
            DevServerTask(wsgi_app=flask),
        ]
    )
    dr.watch()
```

### Tasks
- **Mypy** ✅
- **SimpleHttpServer** ✅
- **Pylint** *TODO*
- **Pytest** *TODO*
- **ISort** *TODO*
- **Flake8** *TODO*
- **Bandit** *TODO*
- **Sphinx** *TODO*
- **Custom Task** *TODO*


