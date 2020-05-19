import configparser
import pytest

from pyjdbcconnector.connectors import DenodoConnector, HiveConnector


def test_denodo():
    config = configparser.ConfigParser()
    config.read("./tests/utils/denodo_config.ini")

    dc = DenodoConnector()
    dc.from_config(config)

    assert dc.connection_url == 'test_url'
    assert dc.username == 'test_username'
    assert dc.password == 'test_password'

    assert dc.trust_store_location == '/trust/store/location'
    assert dc.trust_store_password == 'trust_store_password'

    assert dc.jdbc_location == '/path/to/denodo-vdp-jdbcdriver.jar'
    assert dc.java_classname == 'com.denodo.vdp.jdbc.Driver'


def test_hive():
    config = configparser.ConfigParser()
    config.read("./tests/utils/hive_config.ini")

    dc = HiveConnector()
    dc.from_config(config)

    assert dc.host == 'host.name'
    assert dc.port == 10000
    assert dc.database == 'db'
    assert dc.username == 'test_username'
    assert dc.auth_method == 'KERBEROS'
    assert dc.kerberos_service_name == 'hive'
