import random
import string

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
        try:
            picked_name = content[random.randint(0, len(content) - 1)]
            return picked_name
        except TypeError:
            picked_name = random.choice(string.ascii_uppercase)
            number = 2 + random.randint(1, 4)
            for i in range(number):
                picked_name += random.choice(string.ascii_lowercase)
            return picked_name
