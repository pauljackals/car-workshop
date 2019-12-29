# import random
#
#
# def get_gender_name(number):
#     for gender in __genders:
#         if number == __genders[gender]:
#             return gender
#
#
# def get_gender(gender):
#     return __genders.get(gender)
#
#
# def get_genders():
#     return __genders
#
#
# def get_random_gender():
#     genders = list(__genders.values())
#     return genders[random.randint(0, len(genders))-1]
#
#
# __genders = {
#     "female": 0,
#     "male": 1
# }
from utils.database import Database


def get_gender_name(number):
    return Database.get_element_name('genders', number)


def get_gender(gender):
    return Database.get_element_number('genders', gender)


def get_genders():
    return Database.get_elements('genders')


def get_random_gender():
    return Database.get_element_random('genders')
