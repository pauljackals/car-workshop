from pages.clear_console import clear_console
from pages.load import load
from pages.menu_ingame import menu_ingame
from pages.read_key import read_key
from pages.save import save
from people.client import Client
from people.mechanic import Mechanic
from utils import genders, skills
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
        'turn'
    ]
    left = mechanics
    right = vehicles

    screen = [top, left, right]

    top_length = 0
    for i in top:
        top_length += len(button_names.get(i)) + 4

    pick_row = 0
    pick_element = 0

    while True:
        clear_console()

        middle_to_print = []
        middle_to_print_line = ''
        for i in range(len(screen[0])):
            string = button_names.get(screen[0][i])
            if pick_row == 0 and pick_element == i:
                middle_to_print_line += ">>" + string + "<<"
            else:
                middle_to_print_line += "  " + string + "  "
        middle_to_print.append(middle_to_print_line)
        middle_to_print.append('')

        max_range = max(len(screen[1]), len(screen[2]))
        for i in range(max_range):
            middle_to_print_line = ''
            if i < len(screen[1]):
                element = screen[1][i]
                string = element.get_name_first()
            else:
                string = ''
            if pick_row == 1 and pick_element == i:
                middle_to_print_line += ">>" + string + "<<"
            else:
                middle_to_print_line += "  " + string + "  "

            for j in range(len(string)+4, top_length-7-4):
                middle_to_print_line += ' '

            if i < len(screen[2]):
                string = screen[2][i].get_plate()
            else:
                string = '       '
            if pick_row == 2 and pick_element == i:
                middle_to_print_line += ">>" + string + "<<"
            else:
                middle_to_print_line += "  " + string + "  "
            middle_to_print.append(middle_to_print_line)

        middle_to_print.append('')
        middle_to_print_line = ''
        for i in range(top_length):
            middle_to_print_line += '-'
        middle_to_print.append(middle_to_print_line)

        if pick_row != 0:
            middle_to_print.append('')
            element = screen[pick_row][pick_element]

        if pick_row == 1:
            middle_to_print.append(element.get_name_full())
            middle_to_print.append(genders.get_gender_name(element.get_gender()))
            middle_to_print.append(str(element.get_age())+'yr')
            middle_to_print.append(skills.get_skill_name(element.get_skill()) + " (" + str(element.get_skill()) + ")")
        elif pick_row == 2:
            middle_to_print.append(element.get_plate())
            middle_to_print.append("engine (" + str(element.get_engine().get_status()) + "%)")
            for i in range(len(element.get_wheels())):
                wheel = element.get_wheels()[i]
                middle_to_print.append("wheel " + str(i + 1) + " (" + str(wheel.get_status()) + "%)")
            middle_to_print.append('')
            owner = element.get_owner()
            middle_to_print.append(owner.get_name_full())
            middle_to_print.append(genders.get_gender_name(owner.get_gender()))
            middle_to_print.append(str(owner.get_age()) + 'yr')

        for i in middle_to_print:
            print(i)

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
        elif key == 'ENTER' and pick_row == 0 and screen[0][pick_element] == 'turn':
            new_client = Client(session.generate_new_object_id())
            new_car = Car(session.generate_new_object_id(), session.get_data()['used_plates'].get_new_plate())

            new_car.set_owner(new_client)
            new_client.set_vehicle(new_car)

            clients.append(new_client)
            vehicles.append(new_car)
            pick_element = 0
        elif key == 'm':
            new_mechanic = Mechanic(session.generate_new_object_id())
            mechanics.append(new_mechanic)
        elif pick_row == 0 and key == 'ARROW_LEFT' and pick_element-1 >= 0:
            pick_element -= 1
        elif pick_row == 0 and key == 'ARROW_RIGHT' and pick_element+1 < len(screen[0]):
            pick_element += 1
        elif pick_row == 0 and key == 'ARROW_DOWN':
            if ((pick_element > len(screen[0]) // 2 -1) or (len(screen[1]) <= 0)) and len(screen[2]) > 0:
                pick_row = 2
                pick_element = 0
            elif ((pick_element <= len(screen[0])//2 -1) or (len(screen[2]) <= 0)) and len(screen[1]) > 0:
                pick_row = 1
                pick_element = 0

        elif (pick_row == 1 or pick_row == 2) and key == 'ARROW_UP' and pick_element-1 >= 0:
            pick_element -= 1
        elif (pick_row == 1 or pick_row == 2) and key == 'ARROW_UP' and pick_element-1 < 0:
            if pick_row == 1:
                pick_element = 0
            elif pick_row == 2:
                pick_element = len(screen[0])-1
            pick_row = 0
        elif ((pick_row == 1 and pick_element+1 < len(screen[1]))
              or
              (pick_row == 2 and pick_element+1 < len(screen[2]))) and key == 'ARROW_DOWN':
            pick_element += 1
        elif pick_row == 1 and key == 'ARROW_RIGHT' and len(screen[2]) > 0:
            pick_row = 2
            if pick_element >= len(screen[2]):
                pick_element = len(screen[2])-1
        elif pick_row == 2 and key == 'ARROW_LEFT' and len(screen[1]) > 0:
            pick_row = 1
            if pick_element >= len(screen[1]):
                pick_element = len(screen[1])-1
