from pages.clear_console import clear_console
from pages.read_key import read_key
from people.mechanic import Mechanic


def new(session):
    session.set_new_game(True)
    messages = [
        '*Mechanic Creation*',
        'First name: ',
        'Last name: '
    ]
    name_first = None
    name_last = None
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

        print()
        print('Press ENTER to start')
        key = read_key()
        if key == 'ENTER':
            break

    mechanic = Mechanic(name_first, name_last)
    data = session.get_data()
    data['mechanics'].append(mechanic)
    session.set_data(data)
    return
    # return name_first, name_last
