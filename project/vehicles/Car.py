from people.Client import Client
from vehicles.Vehicle import Vehicle
from vehicles.parts.Engine import Engine


class Car(Vehicle):

    def __init__(self, plate):
        super().__init__(plate, 4)
        self.__owner = None

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner
