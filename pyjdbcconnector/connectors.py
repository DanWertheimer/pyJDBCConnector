from abc import ABC, abstractmethod

import jaydebeapi
import jpype


class BaseConnector(ABC):

    @abstractmethod
    def connect(self, connection_url: str,
                username: str, password: str) -> jaydebeapi.Connection:
        pass

    @abstractmethod
    def disconnect(self):
        pass


class DenodoConnector(BaseConnector):
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

    def connect(
        self, connection_url: str, username: str, password: str
    ) -> jaydebeapi.Connection:
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
                      self.trust_store_password, self.jdbc_location)
            # Create connection
        conn = jaydebeapi.connect(
            jclassname=self.java_classname,
            url=connection_url,
            driver_args=[username, password],
            jars=self.jdbc_location,
        )

        return conn

    def disconnect(self):
        _stopJVM()
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
