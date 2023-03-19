# bkgames

Application identifies the least recently watched teams.

# How to use?

To run the application, navigate to the ```'src'``` folder and execute:

```
python -m bkgames
```

TODO: packages installation (requirements.txt)

# How to install

__Note__: this functionality is in progress, which means that you can install app as a package, but it won't work correctly yet.

```
python setup.py sdist
cd dist
pip install <package_name>
```

# Unit tests

To run unit tests, in the root folder, execute:

```
python -m unittest
```

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
