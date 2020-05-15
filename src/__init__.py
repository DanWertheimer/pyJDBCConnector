from abc import ABC, abstractmethod

__version__ = "0.1.0"


class Connector(ABC):
    @abstractmethod
    def connect(self, connection_url, username, password):
        pass
