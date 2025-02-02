# bkgames

The application lists teams from the most recently to the least recently watched.

Based on the output it can be determined games of which teams to watch next.

Teams to be watched (least watched so far) are displayed at the bottom of the list. The higher the team in the list, the more it has been watched.

# Configuration file

When the application starts, a config file is created in the `~/.bkgames` folder.

Config file in this folder is called `config.json`. You can adjust it to your needs.

Config entries:
- data_file_regexp - regular expression that specifies how file with input data is discovered in the `~/.bkgames/data` folder 
- season_start_month - month in which season starts (used for sorting games)
- allowed_teams - all available teams taken into calculation
- skipped_teams - allows skipping teams not interesting to watch *(when teams to watch are listed, results in an additional annotation to skip this team from watching)*

# Better way to install
With poetry, run:
```
poetry build
```
Wheel is created in the ```./dist``` folder. Go to the ```./dist``` folder and run:
```
pip install wheel_file_name.whl
```

# How to use?

Go to the application folder and execute:

```
python -m bkgames
```

# How to install (deprecated)

In the bkgames folder run:
```
poetry build -f sdist
```

Package is created in the `dist` folder.
To install it run:
```
pip install path_to_tar_gz_file
```

Legacy method (do not use; just for reference here):
```
python setup.py sdist
cd dist
pip install <package_name>
```

# Unit tests

To run unit tests, execute (in the root folder of this repository):

```
pytest
```

# Code coverage

- To show report in command line:
  ```
  coverage report -m
  ```
- To generate html report:
  ```
  coverage html
  ```
