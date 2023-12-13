# bkgames

The application lists teams from the most recently to the least recently watched.

Based on the output it can be determined games of which teams to watch next.

# Configuration file (in progress)
TODO

# How to use?

Go to the application folder and execute:

```
python -m bkgames
```

# How to install (in progress)

__Note__: this functionality is in progress, which means that you can install app as a package, but it won't work correctly yet.

```
python setup.py sdist
cd dist
pip install <package_name>
```

# Unit tests

To run unit tests, in the root folder of this repository, execute:

```
python -m unittest
```
or run:
```
pytest
```

# Code coverage
To check code coverage:

```
coverage run -m unittest
```

and then:

- To show report in command line:
  ```
  coverage report -m
  ```
- To show report in html:
  ```
  coverage html
  ```
