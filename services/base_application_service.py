from abc import ABC, abstractmethod

class BaseApplicationService(ABC):

    def __init__(self):
        pass

    @classmethod
    @abstractmethod
    def get_by_template(cls, template):
        pass

    @classmethod
    @abstractmethod
    def put_by_template(cls, template):
        pass

    @classmethod
    @abstractmethod
    def delete_by_template(cls, template):
        pass
