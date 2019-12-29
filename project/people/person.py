from utils import genders
from utils.age import get_random_age
from utils.names import Names


class Person:

    def __init__(self, name_first=None, name_last=None, gender=None, age=None):
        if gender is None:
            gender = genders.get_random_gender()
        if name_first is None:
            name_first = Names.get_name_first(self.__gender)
        if name_last is None:
            name_last = Names.get_name_last()
        if age is None:
            age = get_random_age()
        self.__gender = gender
        self.__name_first = name_first
        self.__name_last = name_last
        self.__age = age

    def get_name_full(self):
        return self.__name_first + " " + self.__name_last

    def get_name_first(self):
        return self.__name_first

    def get_name_last(self):
        return self.__name_last

    def get_gender(self):
        return self.__gender

    def get_age(self):
        return self.__age

    def print_info(self):
        print(self.get_name_full())
        print(genders.get_gender_name(self.__gender))
        print(str(self.__age)+'yr')
