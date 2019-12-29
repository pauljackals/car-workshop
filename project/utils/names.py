# import random
#
#
# def get_name_first(gender):
#     firstnames = ["firstnames_female", "firstnames_male"]
#     return __get_random_name(firstnames[gender])
#
#
# def get_name_last():
#     return __get_random_name("lastnames")
#
#
# def __get_random_name(key):
#
#     content = __names.get(key)
#     picked_name = content[random.randint(0, len(content)-1)]
#     return picked_name
#
#
# def __read_file(filename):
#
#     with open("resources/" + filename + ".txt", "r") as file:
#         content = file.read().splitlines()
#     return content
#
#
# __names = {
#     "firstnames_female": __read_file("firstnames_female"),
#     "firstnames_male": __read_file("firstnames_male"),
#     "lastnames": __read_file("lastnames")
# }
import random

from utils.file_reader import FileReader


class Names:

    __names = {
        "firstnames_female": FileReader.read_file("firstnames_female"),
        "firstnames_male": FileReader.read_file("firstnames_male"),
        "lastnames": FileReader.read_file("lastnames")
    }

    @staticmethod
    def get_name_first(gender):
        firstnames = ["firstnames_female", "firstnames_male"]
        return Names.__get_random_name(firstnames[gender])

    @staticmethod
    def get_name_last():
        return Names.__get_random_name("lastnames")

    @staticmethod
    def __get_random_name(key):
        content = Names.__names.get(key)
        picked_name = content[random.randint(0, len(content) - 1)]
        return picked_name
