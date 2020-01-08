import os

from pages.clear_console import clear_console
from pages.read_key import read_key


def mechanic_get_data(mechanics):
    data = ''
    for mechanic in mechanics:
        data += str(mechanic.get_id())
        data += ';' + mechanic.get_name_first()
        data += ';' + mechanic.get_name_last()
        data += ';' + str(mechanic.get_gender())
        data += ';' + str(mechanic.get_age())
        data += ';' + str(mechanic.get_skill())
        kits = mechanic.get_kits()
        data += ';' + str(kits[0])
        data += ';' + str(kits[1])
        data += '\n'
    return data


def save(session):
    current_save_number = 0
    save_name = None
    names = []
    directory = None

    try:
        directory = os.listdir("saves")
    except FileNotFoundError:
        os.mkdir("saves")
        directory = os.listdir("saves")
        
    if len(directory) != 0:
        current_save_number = int(directory[-1]) + 1
        for i in directory:
            with open("saves/"+i) as file:
                line = file.readline()
                names.append(line[0:-1])
    while True:
        for i in range(len(names)):
            print(str(i+1) + ". " + names[i])
        if len(directory) == 0:
            print('EMPTY!')
        print('\nType save name: ', end='')
        name = input()
        if name == '':
            clear_console()
            continue
        ok = True
        for i in names:
            if i == name:
                ok = False
                break
        if not ok:
            print("Name in use!")
            read_key()
            clear_console()
        else:
            save_name = name
            break

    with open("saves/"+str(current_save_number), "w") as file:
        file.write(save_name+'\n')

        file.write("MECHANICS\n")
        mechanics = session.get_data()['mechanics']
        data = mechanic_get_data(mechanics)
        file.write(data)
        file.write("END\n")

        file.write("TO_HIRE\n")
        to_hire = session.get_data()['to_hire']
        data = mechanic_get_data(to_hire)
        file.write(data)
        file.write("END\n")

        file.write("VEHICLES\n")
        vehicles = session.get_data()['vehicles']
        data = ''
        for vehicle in vehicles:
            data += str(vehicle.get_id())
            data += ';' + vehicle.get_plate()
            data += ';' + str(vehicle.get_engine().get_status())
            data += ';' + str(len(vehicle.get_wheels()))
            for wheel in vehicle.get_wheels():
                data += ';' + str(wheel.get_status())
            data += ';' + str(vehicle.get_owner().get_id())
            data += '\n'
        file.write(data)
        file.write("END\n")

        file.write("CLIENTS\n")
        clients = session.get_data()['clients']
        data = ''
        for client in clients:
            data += str(client.get_id())
            data += ';' + client.get_name_first()
            data += ';' + client.get_name_last()
            data += ';' + str(client.get_gender())
            data += ';' + str(client.get_age())
            data += ';' + str(client.get_vehicle().get_id())
            data += '\n'
        file.write(data)
        file.write("END\n")

        file.write("TO_FIX\n")
        to_fix = session.get_data()['to_fix']
        data = ''
        for i in to_fix:
            data += (str(i[0].get_id()) + ';' + str(i[1].get_id()) + '\n')
        file.write(data)
        file.write("END\n")

        file.write("NEXT_ID\n")
        file.write(str(session.get_objects_id())+"\n")

        file.write("TURN\n")
        file.write(str(session.get_turn())+"\n")
        file.write("MONEY\n")
        file.write(str(session.get_money())+"\n")

        file.write("KITS\n")
        data = ''
        for i in list(session.get_data()['kits'].keys()):
            data += ';' + str(session.get_data()['kits'][i])
        data = data[1:]+'\n'
        file.write(data)

        file.write("USED_PLATES")
        plates = session.get_data()['used_plates'].get_plates()
        if len(plates) > 0:
            file.write("\n")
            data = ''
            for plate in plates:
                data += ";" + plate
            data = data[1:]
            file.write(data)

    print('Game saved!')
    read_key()
    session.set_stage('menu_ingame')
