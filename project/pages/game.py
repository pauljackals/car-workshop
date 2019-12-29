from pages.clear_console import clear_console
from pages.load import load
from pages.menu_ingame import menu_ingame
from pages.read_key import read_key
from pages.save import save
from people.client import Client
from vehicles.car import Car


def game(session):
    mechanics = session.get_data()['mechanics']
    vehicles = session.get_data()['vehicles']
    clients = session.get_data()['clients']

    while True:
        clear_console()

        print("MECHANICS:")
        for mechanic in mechanics:
            mechanic.print_info()
        print("\nVEHICLES:")
        for vehicle in vehicles:
            vehicle.print_info()
        print("\nCLIENTS:")
        for client in clients:
            client.print_info()

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
