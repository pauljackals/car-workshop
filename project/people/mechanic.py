from utils import skills
from people.person import Person


class Mechanic(Person):

    def __init__(self, name_first=None, name_last=None, gender=None, age=None, skill=None):
        super().__init__(name_first, name_last, gender, age)
        if skill is None:
            skill = skills.get_random_skill()
        self.__skill = skill

    def get_skill(self):
        return self.__skill

    def print_info(self):
        super().print_info()
        print(skills.get_skill_name(self.__skill) + " (" + str(self.get_skill()) + ")")
