Examples
=============

Installation/Usage:
*******************
This package is currently on PyPi and can be installed through:

.. code-block:: bash

   pip install pyjdbcconnector

Connect to a Denodo JDBC with SSL enabled
*****************************************

.. code-block:: python

    """
    This example demonstrates how to use the DenodoConnector
    api for connecting to a Denodo based JDBC with a Trust Store
    file
    """

    from pyjdbcconnector.connectors import DenodoConnector
    import pandas as pd

    # Set constants used to connect to the jdbc

    TRUST_STORE_LOCATION = "path/to/trust_store.jks"
    TRUST_STORE_PASSWORD = "<password>"

    JDBC_LOCATION = "path/to/denodo-vdp-jdbcdriver.jar"
    JAVA_CLASSNAME = "com.denodo.vdp.jdbc.Driver"

    CONNECTION_URL = "jdbc:vdb://<your_denodo_url>:9999/<database>"

    USERNAME = '<user>'
    PASSWORD = '<password'

    # Initialize a DenodoConnector object
    # the DenodoConnector object acts as 
    # a builder.
    dc = DenodoConnector()

    # Here, we build the connection using the built-in
    # builder functions
    conn = dc\
        .configure_jdbc(JDBC_LOCATION)\           # Set the JDBC location and class name
        .require_trust_store()\                   # tells the DenodoConnector we'll need a .jks file
        .set_trust_store(TRUST_STORE_LOCATION,    # pass location and password for .jks file
                         TRUST_STORE_PASSWORD)\
        .connect(CONNECTION_URL,                  # create connection to the jdbc database
                USERNAME,
                PASSWORD)   

    # this connection acts as a normal sql connection and we can use it
    # as we would use any other connection in Python

    # Assuming we want to read a table into a pandas dataframe
    SQL_QUERY = "select * from tablename"
    data = pd.read_sql(SQL_QUERY, conn)


To connect to a JDBC without SSL, omit the lines that require a Trust Store.