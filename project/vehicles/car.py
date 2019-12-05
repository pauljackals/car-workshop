from vehicles.vehicle import Vehicle


class Car(Vehicle):

    def __init__(self):
        super().__init__(4)

    def print_info(self):
        super().print_info()
