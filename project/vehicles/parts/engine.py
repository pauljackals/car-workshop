from vehicles.parts.part import Part


class Engine(Part):
    def __init__(self, status=None):
        super().__init__(status)
