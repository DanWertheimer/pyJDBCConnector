from abc import ABC, abstractmethod
from typing import Optional, Union, Any
import jaydebeapi
import jpype

from pyhive import hive

Connection = Union[jaydebeapi.Connection, hive.Connection]


class BaseConnector(ABC):
    @abstractmethod
    def from_config(self, config) -> 'BaseConnector':
        raise NotImplementedError

    @abstractmethod
    def connect(self) -> Connection:
        """a connect method that returns a connection object
        for a particular module

        :raises NotImplementedError: this method must be implemented
        :return: a connection object which can be used as a query connection to the database
        :rtype: Connection
        """
        raise NotImplementedError

    @abstractmethod
    def disconnect(self):
        """a method to disconnect/close the currently active connection

        :raises NotImplementedError: this method must be implemented
        """
        raise NotImplementedError


class DenodoConnector(BaseConnector):

    def from_config(self, config):
        if config.has_section('connection'):
            self.connection_url = config['connection']['connection_url']
            self.username = config['connection']['username']
            self.password = config['connection']['password']
        else:
            raise AttributeError("'connection' not found")

        if config.has_section('jdbc'):
            self.jdbc_location = config['jdbc']['jdbc_location']
            self.java_classname = config['jdbc']['java_classname']
        else:
            print("could not find 'jdbc' config")

        if config.has_section('trust_store'):
            self.trust_store_location = config['trust_store']['trust_store_location']
            self.trust_store_password = config['trust_store']['trust_store_password']
            self.require_trust_store = True  # type:ignore

        return self

    def configure_jdbc(
        self, jdbc_location: str, java_classname: str = "com.denodo.vdp.jdbc.Driver"
    ) -> "DenodoConnector":
        """sets the jdbc connection information

        :param jdbc_location: location of the jdbc .jar file on your system
        :type jdbc_location: str
        :param java_classname: java class name for the jdbc, defaults to 'com.denodo.vdp.jdbc.Driver' for Denodo
        :type java_classname: str, optional
        :return: a DenodoConnector object
        :rtype: DenodoConnector
        """
        self.jdbc_location = jdbc_location
        self.java_classname = java_classname
        return self

    def set_trust_store(
        self, trust_store_location: str, trust_store_password: str
    ) -> "DenodoConnector":
        """sets the trust store location for SSL connection

        :param trust_store_location: location of the .jks file on system
        :type trust_store_location: str
        :param trust_store_password: password for the .jks file
        :type trust_store_password: str
        :return: a DenodoConnector object
        :rtype: DenodoConnector
        """
        self.trust_store_location = trust_store_location
        self.trust_store_password = trust_store_password
        return self

    def require_trust_store(self) -> "DenodoConnector":
        self.require_trust_store = True  # type: ignore
        return self

    def connect(self) -> jaydebeapi.Connection:
        """connect through a jdbc string

        :param connection_url: a valid jdbc connection string
        :type connection_url: str
        :param username: username to connect to the jdbc source
        :type username: str
        :param password: password to connect to the jdbc source
        :type password: str
        :return: a jaydebeapi connection object which can be read through pandas
        :rtype: jaydebeapi.Connection
        """
        if self.require_trust_store:
            _startJVM(self.trust_store_location,
                      self.trust_store_password,
                      self.jdbc_location)
            # Create connection
        connection = jaydebeapi.connect(
            jclassname=self.java_classname,
            url=self.connection_url,
            driver_args=[self.username, self.password],
            jars=self.jdbc_location,
        )

        self.connection = connection
        return connection

    def disconnect(self):
        _stopJVM()
        self.connection = ''
        return self


class HiveConnector(BaseConnector):
    def from_config(self, config):
        if not 'connection' in config.sections():
            raise AttributeError("connection not found")
        else:
            self.host = config['connection']['host']
            self.port = int(config['connection']['port'])
            self.database = config['connection']['database']
            self.username = config['connection']['username']
            self.auth_method = config['connection']['auth_method']
            self.kerberos_service_name = config['connection']['kerberos_service_name']

        return self

    def connect(self) -> Connection:
        connection = hive.connect(host=self.host,
                                  port=self.port,
                                  database=self.database,
                                  username=self.username,
                                  auth=self.auth_method,
                                  kerberos_service_name=self.kerberos_service_name)
        self.connection = connection
        return connection

    def disconnect(self):
        if self.connection:
            print("ending active session")
            self.connection.close()
            self.connection = ''
        else:
            print("there is no active session")
        return self


def _startJVM(trust_store_location, trust_store_password, jdbc_location):
    # Initialize the JVM
    jvmPath = jpype.getDefaultJVMPath()
    if jpype.isJVMStarted():
        return print("JVM is already running")
    else:
        print("starting JVM")
        jpype.startJVM(
            jvmPath,
            f"-Djavax.net.ssl.trustStore={trust_store_location}",
            f"-Djavax.net.ssl.trustStorePassword={trust_store_password}",
            f"-Djava.class.path={jdbc_location}",
        )


def _stopJVM():
    jpype.shutdownJVM()