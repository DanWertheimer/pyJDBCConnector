[![PyPI version](https://badge.fury.io/py/pyjdbcconnector.svg)](https://badge.fury.io/py/pyjdbcconnector)
[![Documentation Status](https://readthedocs.org/projects/pyjdbcconnector/badge/?version=latest)](https://pyjdbcconnector.readthedocs.io/en/latest/?badge=latest)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)
[![Say Thanks!](https://img.shields.io/badge/Say%20Thanks-!-1EAEDB.svg)](https://saythanks.io/to/danwertheimer@gmail.com)



# pyJDBCConnector
``pyJDBCConnector`` is a high level JDBC connection API that was designed to provide a further abstraction for jdbc connections in python.
This package is designed as an introduction to jdbc connections in Python and as such provides much less customizability with a focus on
accessibility.

## Motivation
This package came about due to intricacies of dealing with the Denodo JDBC driver with SSL enabled.
The ``jaydebeapi`` package that this package is heavily reliant on doesn't provide the ability to specify
the location of a Trust Store file at JVM start-up. This was a big problem for us and we needed to solve this
for analysts with less engineering experience and enable them to get an introduction to Python programming
with familiar data.

## Limitations

- Currently this package has only been tested for the Denodo JDBC driver

# Examples

## Installation/Usage:
This package is currently on PyPi and can be installed through:

```bash
pip install pyjdbcconnector
```

This package is driven primarily through config files.
To understand how config files are set up please see the [Documentation](https://pyjdbcconnector.readthedocs.io/en/latest/)

### Connect to a Denodo JDBC with SSL enabled



```python
"""
This example demonstrates how to use the DenodoConnector
api for connecting to a Denodo based JDBC with a Trust Store
file
"""
import pandas as pd

from pyjdbcconnector.connectors import DenodoConnector

# Initialize a DenodoConnector object
# the DenodoConnector object acts as 
# a builder.
dc = DenodoConnector()

# Here, we build the connection using the built-in
# builder functions
conn = dc\
    .from_config("path/to/denodo_config.ini")\
    .connect()

# this connection acts as a normal sql connection and we can use it
# as we would use any other connection in Python

# Assuming we want to read a table into a pandas dataframe
SQL_QUERY = "select * from tablename"
data = pd.read_sql(SQL_QUERY, conn)
```

To connect to a JDBC without SSL, omit the lines that require a Trust Store.