from people.person import Person


class Client(Person):

    def __init__(self):
        super().__init__()
        self.__vehicle = None

    def get_vehicle(self):
        return self.__vehicle

    def set_vehicle(self, vehicle):
        self.__vehicle = vehicle

    def print_info(self):
        super().print_info()
        print(self.__vehicle.get_plate())
