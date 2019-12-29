# import random
#
#
# def get_skill_name(number):
#     for skill in __levels_of_skill:
#         if number == __levels_of_skill[skill]:
#             return skill
#
#
# def get_skill(skill):
#     return __levels_of_skill.get(skill)
#
#
# def get_random_skill():
#     skills = list(__levels_of_skill.values())
#     return skills[random.randint(0, len(skills))-1]
#
#
# __levels_of_skill = {
#     "novice": 30,
#     "apprentice": 45,
#     "adept": 60,
#     "expert": 75,
#     "master": 90
# }
from utils.database import Database


def get_skill_name(number):
    return Database.get_element_name('skills', number)


def get_skill(skill):
    return Database.get_element_number('skills', skill)


def get_random_skill():
    return Database.get_element_random('skills')
