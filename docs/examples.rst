Examples
=============

Installation/Usage:
*******************
This package is currently on PyPi and can be installed through:

.. code-block:: bash

   pip install pyjdbcconnector

This package is driven primarily through config files.
To understand how config files are set up please see the :ref:`Configuration` page

Connect to a Denodo JDBC with SSL enabled
*****************************************

.. code-block:: python

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


To connect to a JDBC without SSL, omit the lines that require a Trust Store.