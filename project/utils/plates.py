# def register(plate):
#     if __plates.count(plate) == 0:
#         __plates.append(plate)
#         return True
#     else:
#         return False
#
#
# __plates = []


class Plates:

    __plates = []

    @staticmethod
    def register(plate):
        if Plates.__plates.count(plate) == 0:
            Plates.__plates.append(plate)
            return True
        else:
            return False

    @staticmethod
    def set_plates(plates):
        Plates.__plates = plates

    @staticmethod
    def get_plates():
        return Plates.__plates
