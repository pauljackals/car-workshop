import os

from pages.clear_console import clear_console
from pages.read_key import read_key


def save(session):
    current_save_number = 0
    save_name = None
    names = []
    directory = os.listdir("saves")
    if len(directory) != 0:
        current_save_number = int(directory[-1]) + 1
        for i in directory:
            with open("saves/"+i) as file:
                line = file.readline()
                names.append(line[0:-1])
    while True:
        for i in range(len(names)):
            print(str(i+1) + "." + names[i])
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
        for mechanic in mechanics:
            data = ''
            data += mechanic.get_name_first()
            data += ';' + mechanic.get_name_last()
            data += ';' + str(mechanic.get_gender())
            data += ';' + str(mechanic.get_skill())
            file.write(data+'\n')
    print('Game saved!')
    read_key()
    session.set_stage('menu_ingame')
