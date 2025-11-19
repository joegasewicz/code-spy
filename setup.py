from setuptools import setup
from code_spy._version import __version__

with open("README.md", "r") as fh:
    long_description = fh.read()

setup(
    name="code-spy",
    version=__version__,
    description="Watches for file changes & runs tasks against your Python code.",
    packages=["code_spy"],
    py_modules=["code_spy"],
    install_requires=[
        "watchdog",
        "colorama",
        "mypy",
        "pylint",
        "pytest",
    ],
    classifiers=[
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/joegasewicz/dev-runner",
    author="Joe Gasewicz",
    author_email="contact@josef.digital",
)