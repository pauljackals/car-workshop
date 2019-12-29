from utils.database import Database


def get_gender_name(number):
    return Database.get_element_name('genders', number)


def get_gender(gender):
    return Database.get_element_number('genders', gender)


def get_genders():
    return Database.get_elements('genders')


def get_random_gender():
    return Database.get_element_random('genders')
