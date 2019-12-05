import random


def get_name_first(gender):
    firstnames = ["firstnames_female", "firstnames_male"]
    return __get_file(firstnames[gender])


def get_name_last():
    return __get_file("lastnames")


def __get_file(filename):

    if __names.get(filename) is None:
        with open("resources/" + filename + ".txt", "r") as file:
            content = file.read().splitlines()
        __names.update()

    picked_name = content[random.randint(0, len(content)-1)]
    return picked_name


__names = {
    "firstnames_female": None,
    "firstnames_male": None,
    "lastnames": None
}