import random
import string

from people.client import Client
from utils import plates
from vehicles.parts.engine import Engine
from vehicles.parts.wheel import Wheel


class Vehicle:

    def __init__(self, wheel_number):
        self.__plate = self.__random_plate()
        wheels = []
        for i in range(wheel_number):
            wheels.append(Wheel())
        self.__wheels = wheels
        self.__engine = Engine()
        self.__owner = Client()
        self.__owner.set_vehicle(self)

    def set_owner(self, owner):
        self.__owner = owner

    def get_owner(self):
        return self.__owner

    def get_plate(self):
        return self.__plate

    def get_engine(self):
        return self.__engine

    def get_wheels(self):
        return self.__wheels

    def print_info(self):
        print(self.__plate)
        print("engine (" + str(self.__engine.get_status()) + "%)")
        for i in range(len(self.__wheels)):
            wheel = self.__wheels[i]
            print("wheel " + str(i+1) + " (" + str(wheel.get_status()) + "%)")
        print(self.__owner.get_name_full())

    def __random_plate(self):
        while True:
            plate = ""
            for i in range(2):
                plate += random.choice(string.ascii_uppercase)
            for i in range(5):
                plate += random.choice(string.digits)
            if plates.register(plate):
                break
        return plate
