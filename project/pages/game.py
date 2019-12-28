from pages.clear_console import clear_console
from pages.load import load
from pages.menu_ingame import menu_ingame
from pages.read_key import read_key
from pages.save import save


def game(session):
    mechanics = session.get_data()['mechanics']

    while True:
        clear_console()
        for mechanic in mechanics:
            mechanic.print_info()
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
