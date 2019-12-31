import os

from pages.clear_console import clear_console
from pages.read_key import read_key
from people.client import Client
from people.mechanic import Mechanic
from vehicles.car import Car


def mechanic_load(content, content_index, mechanics):
    while content[content_index + 1] != 'END':
        content_index += 1
        mechanic = content[content_index].split(';')
        mechanics.append(
            Mechanic(
                int(mechanic[0]),
                mechanic[1],
                mechanic[2],
                int(mechanic[3]),
                int(mechanic[4]),
                int(mechanic[5]),
                int(mechanic[6]),
                int(mechanic[7])
            )
        )


def load(session):
    directory = os.listdir("saves")
    if len(directory) == 0:
        return False
    session.flush_data()
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
            turn = None
            money = None
            kits = None
            mechanics = []
            to_hire = []
            to_fix = []
            clients = []
            vehicles = []
            plates = []
            next_id = None
            with open('saves/'+str(directory[pick_index])) as file:
                content = file.read().splitlines()
            content_index = 0
            while content_index < len(content):
                if content[content_index] == 'MECHANICS':
                    mechanic_load(content, content_index, mechanics)
                elif content[content_index] == 'TO_HIRE':
                    mechanic_load(content, content_index, to_hire)
                elif content[content_index] == 'CLIENTS':
                    while content[content_index+1] != 'END':
                        content_index += 1
                        client = content[content_index].split(';')
                        clients.append(
                            (
                                Client(
                                    int(client[0]),
                                    client[1],
                                    client[2],
                                    int(client[3]),
                                    int(client[4])
                                ),
                                int(client[5])
                            )
                        )
                elif content[content_index] == 'TO_FIX':
                    while content[content_index+1] != 'END':
                        content_index += 1
                        temp = content[content_index].split(';')
                        for i in range(len(temp)):
                            temp[i] = int(temp[i])
                        to_fix.append(temp)

                elif content[content_index] == 'VEHICLES':
                    while content[content_index+1] != 'END':
                        content_index += 1
                        vehicle = content[content_index].split(';')
                        if int(vehicle[3]) == 4:
                            vehicles.append(
                                (
                                    Car(
                                        int(vehicle[0]),
                                        vehicle[1],
                                        (
                                            int(vehicle[4]),
                                            int(vehicle[5]),
                                            int(vehicle[6]),
                                            int(vehicle[7])
                                        ),
                                        int(vehicle[2])
                                    ),
                                    int(vehicle[8])
                                )
                            )
                elif content[content_index] == 'NEXT_ID':
                    content_index += 1
                    next_id = int(content[content_index])
                elif content[content_index] == 'TURN':
                    content_index += 1
                    turn = int(content[content_index])
                elif content[content_index] == 'MONEY':
                    content_index += 1
                    money = int(content[content_index])
                elif content[content_index] == 'KITS':
                    content_index += 1
                    kits = content[content_index].split(';')
                    for i in range(len(kits)):
                        kits[i] = int(kits[i])
                elif content[content_index] == 'USED_PLATES' and content_index+1 < len(content):
                    content_index += 1
                    plates = content[content_index].split(';')

                content_index += 1

            for i in clients:
                client = i[0]
                vehicle_id = i[1]
                for j in vehicles:
                    vehicle = j[0]
                    if vehicle_id == vehicle.get_id():
                        vehicle.set_owner(client)
                        client.set_vehicle(vehicle)
                        break

            for i in range(len(clients)):
                clients[i] = clients[i][0]

            for i in range(len(vehicles)):
                vehicles[i] = vehicles[i][0]

            for i in range(len(to_fix)):
                vehicle = None
                mechanic = None

                for j in vehicles:
                    if j.get_id() == to_fix[i][0]:
                        vehicle = j
                        break
                for j in mechanics:
                    if j.get_id() == to_fix[i][1]:
                        mechanic = j
                        break
                to_fix[i] = [vehicle, mechanic]

            data = session.get_data()
            data['mechanics'] = mechanics
            data['to_hire'] = to_hire
            data['clients'] = clients
            data['to_fix'] = to_fix
            data['vehicles'] = vehicles
            data['used_plates'].set_plates(plates)
            session.set_objects_id(next_id)
            session.set_turn(turn)
            session.set_money(money)

            for i in range(len(list(data['kits'].keys()))):
                data['kits'][list(data['kits'].keys())[i]] = kits[i]

            session.set_stage('game')
            return True
