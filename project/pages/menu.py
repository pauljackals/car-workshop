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
    pick = 0

    while True:
        clear_console()
        print('CAR WORKSHOP SIMULATOR')
        print()
        for i in range(len(options)):
            if i == pick:
                print('>>' + options_names[options[i]] + '<<')
            else:
                print('  ' + options_names[options[i]])

        key = read_key()

        if key == 'ARROW_DOWN' and pick+1 < len(options):
            pick += 1
        elif key == 'ARROW_UP' and pick-1 >= 0:
            pick -= 1
        elif key == 'ENTER':
            if options[pick] == 'quit':
                clear_console()
                break

        # key1 = read_key()
        # if key1 == '\xe0':
        #     print('ALERT')
        # key2 = read_key()
        # # if base == '\xe0':
        # #     sub = read_key()
        # #
        # #     if sub == 'H':
        # #         key = 'UP_KEY'
        # #     elif sub == 'M':
        # #         key = 'RIGHT_KEY'
        # #     elif sub == 'P':
        # #         key = 'DOWN_KEY'
        # #     elif sub == 'K':
        # #         key = 'LEFT_KEY'
        # print(key1)
        # print(key2)
        # # if key == 'Q':
        # #     break
