from people import skills
from people.person import Person


class Mechanic(Person):

    # def __init__(self, name_first, name_last, skill_number):
    #     super().__init__(name_first, name_last)
    #     self.__skill_number = skill_number
    #     self.__skill = skills.get_skill_name(skill_number)

    def __init__(self, skill_number):
        super().__init__()
        self.__skill_number = skill_number
        self.__skill = skills.get_skill_name(skill_number)

    def get_skill_number(self):
        return self.__skill_number

    def get_skill(self):
        return self.__skill

    def print_info(self):
        super().print_info()
        print(self.get_skill() + " (" + str(self.get_skill_number()) + ")")
