from functions import names


class Person:
    # def __init__(self, name_first, name_last):
    #     self.__name_first = name_first
    #     self.__name_last = name_last

    def __init__(self):
        self.__name_first = names.get_name_first()
        self.__name_last = names.get_name_last()

    def get_name_full(self):
        return self.__name_first + " " + self.__name_last

    def print_info(self):
        print(self.get_name_full())
