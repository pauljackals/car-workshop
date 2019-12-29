import string
import random


class Plates:

    def __init__(self):
        self.__plates = []

    def get_new_plate(self):
        while True:
            plate = ""
            for i in range(2):
                plate += random.choice(string.ascii_uppercase)
            for i in range(5):
                plate += random.choice(string.digits)
            if self.__plates.count(plate) == 0:
                self.__plates.append(plate)
                return plate

    def set_plates(self, plates):
        self.__plates = plates

    def get_plates(self):
        return self.__plates
