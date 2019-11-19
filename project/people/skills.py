def get_skill_name(number):
    for skill in levels_of_skill:
        if number == levels_of_skill[skill]:
            return skill


levels_of_skill = {
    "apprentice": 30,
    "journeyman": 60,
    "master": 90
}
