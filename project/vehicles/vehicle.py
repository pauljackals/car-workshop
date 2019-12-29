import random
import string

from utils.plates import Plates
from vehicles.parts.engine import Engine
from vehicles.parts.wheel import Wheel


class Vehicle:

    def __init__(self, id_vehicle, plate, wheel_number, wheels, engine):
        self.__id = id_vehicle
        self.__plate = plate
        wheels_new = []
        for i in range(wheel_number):
            if wheels is None:
                wheels_new.append(Wheel())
            else:
                wheels_new.append(Wheel(wheels[i]))
        self.__wheels = wheels_new
        if engine is None:
            engine = Engine()
        else:
            engine = Engine(engine)
        self.__engine = engine
        self.__owner = None

    def get_id(self):
        return self.__id

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

