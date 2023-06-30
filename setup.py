import setuptools

# In the package (.egg), config.json file is embedded.
# Key in the package_data argument is the folder in 'src' in which files are placed.
setuptools.setup(
    name="bkgames",
    version="0.0.1",
    description="Bkgames finds teams to watch",
    packages=setuptools.find_packages('src'),
    package_dir={'': 'src'},
    package_data={'bkgames': ['config.json']}
)
