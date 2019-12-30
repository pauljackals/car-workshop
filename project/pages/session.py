from utils.plates import Plates


class Session:
    def __init__(self):
        self.__stage = None
        self.__data = {
            'mechanics': [],
            'vehicles': [],
            'clients': [],
            'used_plates': Plates(),
            'to_hire': []
        }
        self.__objects_id = 0
        self.__turn = 1
        self.__money = 200

    def get_stage(self):
        return self.__stage

    def set_stage(self, stage):
        self.__stage = stage

    def get_turn(self):
        return self.__turn

    def set_turn(self, turn):
        self.__turn = turn

    def get_money(self):
        return self.__money

    def set_money(self, money):
        self.__money = money

    def get_data(self):
        return self.__data

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
