from utils import skills
from people.person import Person


class Mechanic(Person):

    def __init__(self):
        super().__init__()
        self.__skill = skills.get_random_skill()

    def get_skill(self):
        return self.__skill

    def print_info(self):
        super().print_info()
        print(skills.get_skill_name(self.__skill) + " (" + str(self.get_skill()) + ")")
