from utils import genders
from utils.names import Names


class Person:

    def __init__(self, name_first=None, name_last=None, gender_p=None):
        if gender_p is None:
            gender_p = genders.get_random_gender()
        if name_first is None:
            name_first = Names.get_name_first(self.__gender)
        if name_last is None:
            name_last = Names.get_name_last()
        self.__gender = gender_p
        self.__name_first = name_first
        self.__name_last = name_last

    def get_name_full(self):
        return self.__name_first + " " + self.__name_last

    def get_name_first(self):
        return self.__name_first

    def get_name_last(self):
        return self.__name_last

    def get_gender(self):
        return self.__gender

    def print_info(self):
        print(self.get_name_full())
        print(genders.get_gender_name(self.__gender))
