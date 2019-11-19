from vehicles.parts.Engine import Engine
from vehicles.parts.Wheel import Wheel


class Vehicle:

    def __init__(self, plate, wheel_number):
        self.__plate = plate
        self.__wheels = [Wheel] * wheel_number
        self.__engine = Engine

    def get_plate(self):
        return self.__plate
