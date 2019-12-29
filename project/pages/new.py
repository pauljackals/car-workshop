from pages.clear_console import clear_console
from pages.read_key import read_key
from people.mechanic import Mechanic
from utils.genders import get_genders


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
            if temp == '':
                continue
            name_first = temp
        else:
            print(messages[1] + name_first)

        if name_last is None:
            print(messages[2], end='')
            temp = input()
            if temp == '':
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
            temp = input()
            if temp == '':
                continue
            age = temp
        else:
            print(messages[4] + age)

        print()
        print('Press any key to start')
        key = read_key()
        break

    mechanic = Mechanic(id_mechanic, name_first, name_last, gender, age, 30)
    data = session.get_data()
    data['mechanics'].append(mechanic)
    session.set_data(data)
    session.set_stage('game')
    return
