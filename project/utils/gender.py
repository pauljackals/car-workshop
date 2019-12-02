import random


def get_gender_name(number):
    for gender in __genders:
        if number == __genders[gender]:
            return gender


def get_gender(gender):
    return __genders.get(gender)


def get_random_gender():
    genders = list(__genders.values())
    return genders[random.randint(0, len(genders))-1]


__genders = {
    "female": 0,
    "male": 1
}
