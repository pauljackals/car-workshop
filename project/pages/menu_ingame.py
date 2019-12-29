# from pages.clear_console import clear_console
# from pages.read_key import read_key
#
#
# def menu_ingame(session):
#     options_names = {
#         'game': 'Return to game',
#         'menu': 'Main menu',
#         'load': 'Load game',
#         'save': 'Save game'
#     }
#     options = [
#         'game',
#         'save',
#         'load',
#         'menu'
#     ]
#     pick_index = 0
#     pick = options[pick_index]
#
#     while True:
#         clear_console()
#         print('OPTIONS')
#         print()
#         for i in options:
#             if i == pick:
#                 print('>>' + options_names[i] + '<<')
#             else:
#                 print('  ' + options_names[i])
#
#         key = read_key()
#
#         if key == 'ARROW_DOWN' and pick_index+1 < len(options):
#             pick_index += 1
#         elif key == 'ARROW_UP' and pick_index-1 >= 0:
#             pick_index -= 1
#         elif key == 'ENTER':
#             clear_console()
#             session.set_stage(pick)
#             return
#
#         pick = options[pick_index]
from pages.menu_template import menu_template


def menu_ingame(session):

    options_names = {
        'game': 'Return to game',
        'menu': 'Main menu',
        'load': 'Load game',
        'save': 'Save game'
    }
    options = [
        'game',
        'save',
        'load',
        'menu'
    ]
    return menu_template(session, options_names, options, 'OPTIONS')
