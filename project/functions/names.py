import random


def get_name_first():
    with open("resources/firstnames.txt", "r") as file:
        content = file.read().splitlines()
    picked_name = content[random.randint(0, len(content))]
    return picked_name


def get_name_last():
    with open("resources/lastnames.txt", "r") as file:
        content = file.read().splitlines()
    picked_name = content[random.randint(0, len(content))]
    return picked_name
