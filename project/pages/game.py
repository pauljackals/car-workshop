from pages.clear_console import clear_console
from pages.menu_ingame import menu_ingame
from pages.read_key import read_key
from people.mechanic import Mechanic


# def game(**kwargs):
def game(session):
    mechanics = session.get_data()['mechanics']
    # if kwargs['new']:
    #     nf = kwargs['data'][0]
    #     nl = kwargs['data'][1]
    #     mechanics.append(Mechanic(nf, nl))

    while True:
        clear_console()
        for mechanic in mechanics:
            mechanic.print_info()
        key = read_key()
        if key == 'ESC':
            # pick = menu_ingame()
            menu_ingame(session)
            if session.get_stage() == 'menu':
                return 'menu'
