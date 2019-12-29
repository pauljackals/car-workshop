import random


class Part:
    def __init__(self, status):
        if status is None:
            status = self.__random_status()
        self.__status = status

    def get_status(self):
        return self.__status

    def __random_status(self):
        return random.randint(1, 100)