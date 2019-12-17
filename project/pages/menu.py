from pages.clear_console import clear_console
from pages.read_key import read_key


def menu():
    options_names = {
        'quit': 'Quit',
        'new': 'New game',
        'load': 'Load game'
    }
    options = [
        'new',
        'load',
        'quit'
    ]
    pick_index = 0
    pick = options[pick_index]

    while True:
        clear_console()
        print('CAR WORKSHOP SIMULATOR')
        print()
        for i in options:
            if i == pick:
                print('>>' + options_names[i] + '<<')
            else:
                print('  ' + options_names[i])

        key = read_key()

        if key == 'ARROW_DOWN' and pick_index+1 < len(options):
            pick_index += 1
        elif key == 'ARROW_UP' and pick_index-1 >= 0:
            pick_index -= 1
        elif key == 'ENTER':
            if pick == 'load':
                continue
            clear_console()
            return pick
        pick = options[pick_index]
