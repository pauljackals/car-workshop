class FileReader:

    @staticmethod
    def read_file(filename):
        with open("resources/" + filename + ".txt", "r") as file:
            content = file.read().splitlines()
        return content
