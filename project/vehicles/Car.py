from people.Client import Client
from vehicles.Vehicle import Vehicle
from vehicles.parts.Engine import Engine


class Car(Vehicle):

    def __init__(self, plate, color):
        super().__init__(plate, 4, color)
        self.__owner = None

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def print_info(self):
        super().print_info()
        print(self.get_owner().get_name_full())
