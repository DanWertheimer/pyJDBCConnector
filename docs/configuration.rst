Configuration File
-------------------
The high level api for this package is config driven. This means that certain connections
will require different config values.

DenodoConnector
###############

[jdbc]
***********************

.. confval:: jdbc_location

   :type: string

   location of the jdbc file

.. confval:: java_classname

   :type: string
   :default: ``com.denodo.vdp.jdbc.Driver``

   the main class for the jdbc file


[trust_store]
***********************

.. confval:: trust_store_location

   :type: string

   location of the trust store (.jks) file

.. confval:: trust_store_password

   :type: string

   password for the trust store

[connection]
***********************

.. confval:: connection_url

   :type: string

   connection string for the database you're connecting to

.. confval:: username

   :type: string

   username for the connection

.. confval:: password

   :type: string

   password for the connection

HiveConnector
###############

[connection]
***********************

.. confval:: host

   :type: string

   host connection url

.. confval:: port

   :type: string
   :default: ``10000``

   port that hive is located on

.. confval:: database

   :type: string

   database on the hive server

.. confval:: username

   :type: string

   kerberos username

.. confval:: auth_method

   :type: string
   :default: ``KERBEROS``

   Type of authentication on the hive server

.. confval:: kerberos_service_name

   :type: string
   :default: ``hive``

   service name for kerberos