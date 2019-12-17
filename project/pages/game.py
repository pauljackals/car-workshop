from pages.clear_console import clear_console
from pages.menu_ingame import menu_ingame
from pages.read_key import read_key
from people.mechanic import Mechanic


def game(**kwargs):
    mechanics = []
    if kwargs['new']:
        nf = kwargs['data'][0]
        nl = kwargs['data'][1]
        mechanics.append(Mechanic(nf, nl))

    while True:
        clear_console()
        for mechanic in mechanics:
            mechanic.print_info()
        key = read_key()
        if key == 'ESC':
            pick = menu_ingame()
            if pick == 'menu':
                return 'menu'
