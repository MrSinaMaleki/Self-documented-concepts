from abc import ABC, abstractmethod


class BaseHuman(ABC):
    # instance method

    @abstractmethod
    def say_hello(self):
        raise NotImplementedError

    @classmethod
    @abstractmethod
    def get_id(cls):
        if cls != BaseHuman:
            raise TypeError("class method implementation error")
        raise NotImplementedError

    @property
    @abstractmethod
    def birth_date(self):
        raise NotImplementedError

    @classmethod
    @property
    @abstractmethod
    def birth_date_of_class(cls):
        raise NotImplementedError

    def get_age(self):
        return 2024 - self.birth_date


class Sina(BaseHuman):
    birth_date = 2000

    def get_id(self):
        return "id ---- "

    def thinking(self):
        print("Sina, thinking  -. -.")

    def say_hello(self):
        print("Sina, Hello !")


sina = Sina()
sina.say_hello()
