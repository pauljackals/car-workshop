import random


class Database:

    __content = {
        'genders': {
            "female": 0,
            "male": 1
        },
        'skills': {
            "novice": 30,
            "apprentice": 45,
            "adept": 60,
            "expert": 75,
            "master": 90
        }
    }

    @staticmethod
    def get_element_name(key, number):
        for element in Database.__content.get(key):
            if number == Database.__content.get(key).get(element):
                return element

    @staticmethod
    def get_element_number(key, element):
        return Database.__content.get(key).get(element)

    @staticmethod
    def get_element_random(key):
        elements = list(Database.__content.get(key).values())
        return elements[random.randint(0, len(elements)-1)]

    @staticmethod
    def get_elements(key):
        return Database.__content.get(key)
