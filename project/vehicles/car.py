from vehicles.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self, id_car, plate, wheels=None, engine=None):
        super().__init__(id_car, plate, 4, wheels, engine)

    def print_info(self):
        super().print_info()
