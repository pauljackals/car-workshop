from vehicles.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super().__init__(4)
        self.__owner = None

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def print_info(self):
        super().print_info()
        print(self.get_owner().get_name_full())
