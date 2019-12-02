import random


def get_name_first(gender):
    firstnames = ["firstnames_female.txt", "firstnames_male.txt"]
    return __get_file(firstnames[gender])


def get_name_last():
    return __get_file("lastnames.txt")


def __get_file(filename):
    with open("resources/" + filename, "r") as file:
        content = file.read().splitlines()
    picked_name = content[random.randint(0, len(content)-1)]
    return picked_name
