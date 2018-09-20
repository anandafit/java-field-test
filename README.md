Paython-boilerpalte-pacakge
==========================

##Boilerpalte Pacakge

Basic structure of package is

```
├── README.md
├── cakedoctor
│   ├── __init__.py
│   ├── cakedoctor.py
│   ├── cakedoctor_listener.py
│   ├── event.py
│   ├── orchestration_registry
        ├── __init__.py
        ├── registry.py
│   ├── specialists
        ├── __init__.py
        ├── touch
            ├── __init__.py
            ├── executor.py        
│   └── version.py
├── pytest.ini
├── requirements.txt
├── setup.py
└── tests
    ├── __init__.py
    ├── helpers
    │   ├── __init__.py
    │   └── my_helper.py
    ├── tests_helper.py
    └── unit
        ├── __init__.py
        ├── test_example.py
        └── test_version.py
```

## Requirements

Package requirements are handled using pip. To install them do

```
pip install -r requirements.txt
```

## Tests

Testing is set up using [pytest](http://pytest.org) and coverage is handled
with the pytest-cov plugin.

Run your tests with ```py.test``` in the root directory.

Coverage is ran by default and is set in the ```pytest.ini``` file.
To see an html output of coverage open ```htmlcov/index.html``` after running the tests.

To run the unit test from root dir, run the following, 
```python -m pytest```

## Travis CI

There is a ```.travis.yml``` file that is set up to run your tests for python 2.7
and python 3.2, should you choose to use it.

## How to create cakedoctor distributed pacakges

Make sure you have the latest versions of setuptools and wheel installed:
```python -m pip install --user --upgrade setuptools wheel```

Now run this command from the same directory where setup.py is located to genarate distributed pacakges
```python setup.py sdist bdist_wheel```

This command should output a lot of text and once completed should generate two files in the dist directory:

## Remove pycache files and folders
``` find . | grep -E "(__pycache__|\.pyc|\.pyo$)" | xargs rm -rf ```

## The Best Practices while coding
Cakedoctor is following Google Python Style Guide  https://github.com/google/styleguide/blob/gh-pages/pyguide.md#38-comments-and-docstrings