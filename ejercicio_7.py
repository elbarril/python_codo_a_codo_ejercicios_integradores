from ejercicio_6 import Person

class Account:
    def __init__(self, titular:Person=None, amount:float=None) -> None:
        self.__titular:Person|None = titular
        self.__amount:float|None = amount

    @property
    def titular(self) -> Person|None:
        if not self.__titular is None:
            return self.__titular

    @titular.setter
    def titular(self, titular:Person) -> None:
        self.__titular = titular

    @property
    def amount(self) -> float|None:
        if not self.__amount is None:
            return self.__amount

    @property
    def __amount__(self) -> float|None:
        if not self.__amount is None:
            return self.__amount

    @__amount__.setter
    def __amount__(self, amount:float) -> None:
        self.__amount = amount

    def deposit(self, amount:float) -> None:
        if self.titular is None:
            print("There is not titular.")
        elif Account.__validate_amount(amount):
            self.__amount__ = self.amount + amount if self.amount else amount

    def extract(self, amount:float) -> float|None:
        if self.titular is None:
            print("There is not titular.")
        elif Account.__validate_amount(amount):
            self.__amount__ = self.__amount__ - amount
            return amount

    @classmethod
    def __validate_amount(self, amount:float) -> bool:
        return True if amount >= 0 else False