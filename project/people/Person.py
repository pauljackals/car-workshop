class Person:
    def __init__(self, name_first, name_last):
        self.__name_first = name_first
        self.__name_last = name_last

    def get_name(self):
        return self.__name_first, self.__name_last
