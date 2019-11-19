from vehicles.parts.Engine import Engine
from vehicles.parts.Wheel import Wheel


class Vehicle:

    def __init__(self, plate, wheel_number, color):
        self.__plate = plate
        self.__wheels = [Wheel(100)] * wheel_number
        self.__engine = Engine(100)
        self.__color = color

    def get_plate(self):
        return self.__plate

    def get_engine(self):
        return self.__engine

    def get_wheels(self):
        return self.__wheels

    def print_info(self):
        print(self.get_plate())
        print("engine (" + str(self.get_engine().get_status()) + ")")
        for i in range(len(self.get_wheels())):
            wheel = self.get_wheels()[i]
            print("wheel " + str(i+1) + " (" + str(wheel.get_status()) + ")")
