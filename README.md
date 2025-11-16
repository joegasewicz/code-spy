# Dev Runner
Development tools that watches for file changes within your codebase & runs tasks to check & rerun your Python code.

### Examples

```python
from dev_runner.dev_runner import DevRunner
from dev_runner.tasks import MyPyTask

dr = DevRunner(
    path="examples",
    tasks=[
        MyPyTask(path="examples"),
    ])

if __name__ == "__main__":
    dr.watch()

```