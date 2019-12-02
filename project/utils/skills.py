import random


def get_skill_name(number):
    for skill in __levels_of_skill:
        if number == __levels_of_skill[skill]:
            return skill


def get_skill(skill):
    return __levels_of_skill.get(skill)


def get_random_skill():
    skills = list(__levels_of_skill.values())
    return skills[random.randint(0, len(skills))-1]


__levels_of_skill = {
    "apprentice": 30,
    "journeyman": 60,
    "master": 90
}
