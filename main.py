from dev_runner.dev_runner import DevRunner

dr = DevRunner(path="examples", file="examples/main.py")


if __name__ == "__main__":
    dr.watch()
