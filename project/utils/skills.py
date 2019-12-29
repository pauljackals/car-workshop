from utils.database import Database


def get_skill_name(number):
    return Database.get_element_name('skills', number)


def get_skill(skill):
    return Database.get_element_number('skills', skill)


def get_random_skill():
    return Database.get_element_random('skills')
