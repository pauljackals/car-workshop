import os

from pages.clear_console import clear_console
from pages.read_key import read_key
from people.mechanic import Mechanic


def load(session):
    directory = os.listdir("saves")
    if len(directory) == 0:
        return False
    names = []
    if len(directory) != 0:
        for i in directory:
            with open("saves/"+i) as file:
                line = file.readline()
                names.append(line[0:-1])

    pick_index = 0
    while True:
        clear_console()
        for i in range(len(names)):
            if i == pick_index:
                print(">>", end='')
            else:
                print("  ", end='')
            print(str(i + 1) + ". " + names[i])

        key = read_key()

        if key == 'ARROW_DOWN' and pick_index + 1 < len(names):
            pick_index += 1
        elif key == 'ARROW_UP' and pick_index - 1 >= 0:
            pick_index -= 1
        elif key == 'ENTER':
            content = None
            mechanics = []
            mechanics_start_index = None
            with open('saves/'+str(directory[pick_index])) as file:
                content = file.read().splitlines()
            for i in range(len(content)):
                if content[i] == 'MECHANICS':
                    mechanics_start_index = i+1
                    break
            for i in content[mechanics_start_index:]:
                mechanic = i.split(';')
                mechanics.append(Mechanic(mechanic[0], mechanic[1], int(mechanic[2]), int(mechanic[3])))
            data = session.get_data()
            data['mechanics'] = mechanics
            session.set_data(data)
            session.set_stage('game')
            return True
