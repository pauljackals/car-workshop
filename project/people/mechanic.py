from utils import skills
from people.person import Person


class Mechanic(Person):

    def __init__(self, id_mechanic, name_first=None, name_last=None, gender=None, age=None, skill=None, kits_wheel=0, kits_engine=0):
        super().__init__(id_mechanic, name_first, name_last, gender, age)
        if skill is None:
            skill = skills.get_random_skill()
        self.__skill = skill
        self.__kits_engine = kits_engine
        self.__kits_wheel = kits_wheel

    def get_skill(self):
        return self.__skill

    def prepare(self, session, vehicle):
        status = self.__kits_engine + self.__kits_wheel
        if vehicle.get_engine().get_status() < 100 and session.get_data()['kits']['engine'] > 0:
            session.get_data()['kits']['engine'] -= 1
            self.__kits_engine += 1
        for wheel in vehicle.get_wheels():
            if wheel.get_status() < 100:
                if session.get_data()['kits']['wheel'] > 0:
                    session.get_data()['kits']['wheel'] -= 1
                    self.__kits_wheel += 1
                else:
                    break
        if status != self.__kits_engine + self.__kits_wheel:
            return True
        return False

    def repair(self, vehicle):
        if self.__kits_engine > 0:
            self.__kits_engine -= 1
            vehicle.get_engine().set_status(100)
        for wheel in vehicle.get_wheels():
            if wheel.get_status() < 100:
                self.__kits_wheel -= 1
                wheel.set_status(100)
            if self.__kits_wheel == 0:
                break

    def get_kits(self):
        return self.__kits_wheel, self.__kits_engine

    def set_kits(self, kits):
        self.__kits_wheel = kits[0]
        self.__kits_engine = kits[1]

    def print_info(self):
        super().print_info()
        print(skills.get_skill_name(self.__skill) + " (" + str(self.get_skill()) + ")")
