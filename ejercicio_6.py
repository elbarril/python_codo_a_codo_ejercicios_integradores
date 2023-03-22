class Person:
    def __init__(self, name:str='', age:str|int='', uid:str|int=''):
        if (not age or Person.__is_valid_age(age)) and (not uid or Person.__is_valid_uid(uid)) and (not name or Person.__is_valid_name(name)):
            self.__name:str = name
            self.__age:str|int = age
            self.__uid:str|int = uid
        else:
            raise Exception("Wrong type parameters.")

    @property
    def name(self) -> str:
        if self.__name:
            return self.__name
    
    @name.setter
    def name(self, name:str) -> None:
        if Person.__is_valid_name(name):
            self.__name = name
        else:
            print("The name is not a valid name.")

    @property
    def age(self) -> int:
        if self.__age:
            return int(self.__age)
    
    @age.setter
    def age(self, age:str|int) -> None:
        if Person.__is_valid_age(age):
            self.__age = int(age)
        else:
            print("The age is not a valid number.")

    @property
    def uid(self) -> int:
        if self.__uid:
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

    def is_adult(self):
        if self.age:
            return self.age >= 18
        
    @classmethod
    def __is_valid_name(self, name):
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
    def __is_valid_number(self, number):
        try:
            int(number)
            return True
        except:
            return False