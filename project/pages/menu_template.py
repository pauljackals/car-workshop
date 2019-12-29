from pages.clear_console import clear_console
from pages.read_key import read_key


def menu_template(session, options_names, options, header):
    options_names_local = options_names
    options_local = options
    pick_index = 0
    pick = options_local[pick_index]

    while True:
        clear_console()
        print(header)
        print()
        for i in options_local:
            if i == pick:
                print('>>' + options_names_local[i] + '<<')
            else:
                print('  ' + options_names_local[i])

        key = read_key()

        if key == 'ARROW_DOWN' and pick_index+1 < len(options_local):
            pick_index += 1
        elif key == 'ARROW_UP' and pick_index-1 >= 0:
            pick_index -= 1
        elif key == 'ENTER':
            clear_console()
            session.set_stage(pick)
            return

        pick = options_local[pick_index]
