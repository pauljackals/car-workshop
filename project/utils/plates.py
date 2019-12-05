def register(plate):
    if __plates.count(plate) == 0:
        __plates.append(plate)
        return True
    else:
        return False


__plates = []
