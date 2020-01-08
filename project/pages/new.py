from pages.clear_console import clear_console
from pages.read_key import read_key
from people.client import Client
from people.mechanic import Mechanic
from utils.genders import get_genders
from vehicles.car import Car


def check_for_illegal_characters(string, *args):
    for character in string:
        for illegal in args:
            if character == illegal:
                return False
    return True


def new(session):
    session.flush_data()
    messages = [
        '*Mechanic Creation*',
        'First name: ',
        'Last name: ',
        'Gender: ',
        'Age: '
    ]
    id_mechanic = session.generate_new_object_id()
    name_first = None
    name_last = None
    gender = None
    genders = get_genders()
    genders_keys = list(genders.keys())
    gender_index = 0
    age = None
    while True:
        clear_console()
        print(messages[0])
        print()
        if name_first is None:
            print(messages[1], end='')
            temp = input()

            if temp == '' or not check_for_illegal_characters(temp, ';', ' '):
                continue
            name_first = temp
        else:
            print(messages[1] + name_first)

        if name_last is None:
            print(messages[2], end='')
            temp = input()
            if temp == '' or not check_for_illegal_characters(temp, ';', ' '):
                continue
            name_last = temp
        else:
            print(messages[2] + name_last)

        if gender is None:
            print(messages[3], end='')
            for i in range(len(genders_keys)):
                if i == gender_index:
                    print('>', end='')
                else:
                    print(' ', end='')
                print(genders_keys[i], end='')
                if i == gender_index:
                    print('<', end='')
                else:
                    print(' ', end='')
            print()
            key = read_key()
            if key == 'ARROW_RIGHT' and gender_index+1 < len(genders_keys):
                gender_index += 1
            elif key == 'ARROW_LEFT' and gender_index-1 >= 0:
                gender_index -= 1
            elif key == 'ENTER':
                gender = genders.get(genders_keys[gender_index])
            continue
        else:
            print(messages[3] + genders_keys[gender_index])

        if age is None:
            print(messages[4], end='')
            try:
                temp = int(input())
            except ValueError:
                continue
            if temp == '' or temp < 18:
                continue
            age = temp
        else:
            print(messages[4] + age)

        print()
        print('Press any key to start')
        read_key()
        break

    mechanic = Mechanic(id_mechanic, name_first, name_last, gender, age, 30)
    data = session.get_data()
    data['mechanics'].append(mechanic)

    new_client = Client(session.generate_new_object_id())
    new_car = Car(session.generate_new_object_id(), session.get_data()['used_plates'].get_new_plate())
    new_car.set_owner(new_client)
    new_client.set_vehicle(new_car)

    data['clients'].append(new_client)
    data['vehicles'].append(new_car)

    session.set_stage('game')
    return
