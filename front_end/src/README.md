# Front end code base

> Note: the sys.path *is* dirty but I'm running of clean way

## Directory structure

I try to keep it small.
Utils component will be subdivided into their own modules

```txt
   |-- Dockerfile
   |-- README.md
   |-- pyproject.toml
   |-- src
   |   |-- README.md
   |   |-- __init__.py
   |   |-- main.py
   |   |-- pages // Pages script, prefix file name with number-
   |   |   |-- __init__.py
   |   |-- utils // Utilities such as logging, testing, fetch, and types
   |   |   |-- __init__.py
   |   |-- widgets // Self explanatory
   |   |   |-- __init__.py
   |-- uv.lock
```
