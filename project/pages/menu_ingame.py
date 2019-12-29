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
