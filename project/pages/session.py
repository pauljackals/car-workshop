class Session:
    def __init__(self):
        self.__stage = None
        self.__data = {
            'mechanics': []
        }

    def get_stage(self):
        return self.__stage

    def set_stage(self, stage):
        self.__stage = stage

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def flush_data(self):
        self.__data = {
            'mechanics': []
        }
