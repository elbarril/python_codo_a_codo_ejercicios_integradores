class Person:
    def __init__(self, name:str|None=None, age:str|int|None=None, uid:str|int|None=None):
        if (age is None or Person.__is_valid_age(age)) and (uid is None or Person.__is_valid_uid(uid)) and (name is None or Person.__is_valid_name(name)):
            self.__name:str|None = name
            self.__age:str|int|None = age
            self.__uid:str|int|None = uid
        else:
            raise Exception("Wrong type parameters.")

    @property
    def name(self) -> str|None:
        if not self.__name is None:
            return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        if Person.__is_valid_name(name):
            self.__name = name
        else:
            print("The name is not a valid name.")

    @property
    def age(self) -> int|None:
        if not self.__age is None:
            return int(self.__age)
    
    @age.setter
    def age(self, age:str|int) -> None:
        if Person.__is_valid_age(age):
            self.__age = int(age)
        else:
            print("The age is not a valid number.")

    @property
    def uid(self) -> int|None:
        if not self.__uid is None:
            return int(self.__uid)
    
    @uid.setter
    def uid(self, uid:str|int) -> None:
        if Person.__is_valid_uid(uid):
            self.__uid = int(uid)
        else:
            print("The unique ID is not a valid number.")

    def show(self) -> None:
        print("name:", self.name)
        print("age:", self.age)
        print("uid:", self.uid)

    def is_adult(self) -> bool|None:
        if not self.age is None:
            return self.age >= 18
        
    @classmethod
    def __is_valid_name(self, name:str) -> bool:
        name = str(name)
        if len(name):
            for letter in name:
                try:
                    int(letter)
                    return False
                except:
                    pass
            return True

    @classmethod
    def __is_valid_age(self, age:str|int) -> bool:
        if Person.__is_valid_number(age):
            return 0 <= int(age) < 120
        else:
            return False

    @classmethod
    def __is_valid_uid(self, uid:str|int) -> bool:
        if Person.__is_valid_number(uid):
            return 9 > len(str(uid)) > 7
        else:
            return False
        
    @classmethod
    def __is_valid_number(self, number:str|int) -> bool:
        try:
            int(number)
            return True
        except:
            return False