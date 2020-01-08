class FileReader:

    @staticmethod
    def read_file(filename):
        try:
            with open("resources/" + filename + ".txt", "r") as file:
                content = file.read().splitlines()
            return content
        except FileNotFoundError:
            return None
