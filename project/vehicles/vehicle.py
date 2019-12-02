import random
import string

from vehicles.parts.engine import Engine
from vehicles.parts.wheel import Wheel


class Vehicle:

    def __init__(self, wheel_number):
        self.__plate = self.__random_plate()
        self.__wheels = [Wheel(100)] * wheel_number
        self.__engine = Engine(100)

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

    def __random_plate(self):
        plate = ""
        for i in range(2):
            plate += random.choice(string.ascii_uppercase)
        for i in range(5):
            plate += random.choice(string.digits)
        return plate
