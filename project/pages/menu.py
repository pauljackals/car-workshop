from pages.menu_template import menu_template


def menu(session):

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
    return menu_template(session, options_names, options, 'CAR WORKSHOP SIMULATOR')
