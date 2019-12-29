from people.person import Person


class Client(Person):

    def __init__(self, id_client, name_first=None, name_last=None, gender=None, age=None):
        super().__init__(id_client, name_first, name_last, gender, age)
        self.__vehicle = None

    def get_vehicle(self):
        return self.__vehicle

    def set_vehicle(self, vehicle):
        self.__vehicle = vehicle

    def print_info(self):
        super().print_info()
        print(self.__vehicle.get_plate())
