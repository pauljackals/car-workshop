class Session:
    def __init__(self):
        self.__player = None
        self.__new_game = None
        self.__stage = 'menu'
        self.__data = {
            'mechanics': []
        }

    def get_stage(self):
        return self.__stage

    def set_stage(self, stage):
        self.__stage = stage

    def get_player(self):
        return self.__player

    def set_player(self, player):
        self.__player = player

    def get_data(self):
        return self.__data

    def set_data(self, data):
        self.__data = data

    def get_new_game(self):
        return self.__new_game

    def set_new_game(self, new_game):
        self.__new_game = new_game
