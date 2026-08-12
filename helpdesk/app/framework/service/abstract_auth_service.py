from abc import ABC, abstractmethod


class AbstractAuthService(ABC):
    @staticmethod
    @abstractmethod
    def insert(form):
        pass
