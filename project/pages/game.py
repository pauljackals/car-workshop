from pages.clear_console import clear_console
from pages.load import load
from pages.menu_ingame import menu_ingame
from pages.read_key import read_key
from pages.save import save
from people.client import Client
from people.mechanic import Mechanic
from vehicles.car import Car


def game(session):
    mechanics = session.get_data()['mechanics']
    vehicles = session.get_data()['vehicles']
    clients = session.get_data()['clients']

    button_names = {
        'turn': 'New turn',
        'placeholder': 'placeholder'
    }

    top = [
        'placeholder',
        'placeholder',
        'placeholder',
        'placeholder',
        'turn'
    ]
    left = mechanics
    right = clients

    screen = [top, left, right]

    pick_row = 0
    pick_element = 0

    while True:
        clear_console()

        # print("MECHANICS:")
        # for mechanic in mechanics:
        #     mechanic.print_info()
        # print("\nVEHICLES:")
        # for vehicle in vehicles:
        #     vehicle.print_info()
        # print("\nCLIENTS:")
        # for client in clients:
        #     client.print_info()

        for i in range(len(screen[0])):
            string = button_names.get(screen[0][i])
            if pick_row == 0 and pick_element == i:
                print(">>" + string + "<<", end='')
            else:
                print("  " + string + "  ", end='')
        print()
        print()

        strings = []
        for i in range(len(screen[1])):
            element = screen[1][i]
            strings.append(element.get_name_first() + " " + element.get_name_last())
        max_len = 50

        for i in range(len(screen[1])):
            string = strings[i]
            if pick_row == 1 and pick_element == i:
                print(">>" + string + "<<", end='')
            else:
                print("  " + string + "  ", end='')
            for j in range(len(string)+4, max_len+1):
                print(' ', end='')
            print('bing_bong', end='')
            print()

        # for i in range(len(screen)):
        #     var = ''
        #     if i != 0:
        #         var = '\n'
        #     for j in range(len(screen[i])):
        #         element = screen[i][j]
        #         string = ''
        #         type_name = type(element).__name__
        #         if type_name == 'str':
        #             string = button_names.get(element)
        #         elif type_name == 'Mechanic':
        #             string = element.get_name_first() + " " + element.get_name_last()
        #         elif type_name == 'Car':
        #             string = element.get_plate()
        #         if pick_row == i and pick_element == j:
        #             print(">>"+string+"<<", end=var)
        #         else:
        #             print("  "+string+"  ", end=var)
        #     if i == 0:
        #         print()

        key = read_key()
        if key == 'ESC':
            while True:
                menu_ingame(session)
                if session.get_stage() == 'menu':
                    return 'menu'
                elif session.get_stage() == 'save':
                    save(session)
                elif session.get_stage() == 'load':
                    if not load(session):
                        print('No save files!')
                        read_key()
                    else:
                        return
                else:
                    break
        elif key == 'n':
            new_client = Client(session.generate_new_object_id())
            new_car = Car(session.generate_new_object_id(), session.get_data()['used_plates'].get_new_plate())

            new_car.set_owner(new_client)
            new_client.set_vehicle(new_car)

            clients.append(new_client)
            vehicles.append(new_car)
        elif key == 'm':
            new_mechanic = Mechanic(session.generate_new_object_id())
            mechanics.append(new_mechanic)
        elif pick_row == 0 and key == 'ARROW_LEFT' and pick_element-1 >= 0:
            pick_element -= 1
        elif pick_row == 0 and key == 'ARROW_RIGHT' and pick_element+1 < len(screen[0]):
            pick_element += 1
        elif pick_row == 0 and key == 'ARROW_DOWN':
            pick_row += 1
            pick_element = 0

        elif pick_row == 1 and key == 'ARROW_UP' and pick_element-1 >= 0:
            pick_element -= 1
        elif pick_row == 1 and key == 'ARROW_UP' and pick_element-1 < 0:
            pick_row -= 1
            pick_element = 0
        elif pick_row == 1 and key == 'ARROW_DOWN' and pick_element+1 < len(screen[1]):
            pick_element += 1
