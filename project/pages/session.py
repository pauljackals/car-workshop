from utils.plates import Plates


class Session:
    def __init__(self):
        self.__stage = None
        self.__data = {
            'mechanics': [],
            'vehicles': [],
            'clients': [],
            'used_plates': Plates()
        }
        self.__objects_id = 0

    def get_stage(self):
        return self.__stage

    def set_stage(self, stage):
        self.__stage = stage

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def set_objects_id(self, objects_id):
        self.__objects_id = objects_id

    def generate_new_object_id(self):
        new_id = self.__objects_id
        self.__objects_id = new_id + 1
        return new_id

    def get_objects_id(self):
        return self.__objects_id

    def flush_data(self):
        stage = self.__stage
        self.__init__()
        self.set_stage(stage)
