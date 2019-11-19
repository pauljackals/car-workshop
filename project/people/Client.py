from people.Person import Person


class Client(Person):

    def __init__(self, name_first, name_last):
        super().__init__(name_first, name_last)
        self.__vehicle = None

    def get_vehicle(self):
        return self.__vehicle

    def set_vehicle(self, vehicle):
        self.__vehicle = vehicle
