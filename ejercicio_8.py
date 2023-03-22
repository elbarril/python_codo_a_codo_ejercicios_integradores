from ejercicio_6 import Person
from ejercicio_7 import Account

class YoungAccount(Account):
    def __init__(self, titular:Person=None, amount:float=None, bonification:float=None) -> None:
        super().__init__(titular, amount)
        self.__bonification:float|None = bonification if YoungAccount.__validate_percentage(bonification) or bonification is None else None

    @property
    def bonification(self) -> float|None:
        if self.__bonification:
            return self.__bonification

    @bonification.setter
    def bonification(self, bonification:float) -> None:
        if YoungAccount.__validate_percentage(bonification):
            self.__bonification = bonification
        else:
            print("This is not a valid percentage value")

    def extract(self, amount: float) -> float | None:
        if YoungAccount.is_valid_titular:
            return super().extract(amount)
    
    def show(self):
        print("Young Account")
        print("{:.0%}".format(self.bonification))

    @classmethod
    def is_valid_titular(self):
        return True if self.titular and self.titular.age > 25 else False

    @classmethod
    def __validate_percentage(self, bonification:float) -> bool:
        return True if 0 <= bonification <= 1 else False
