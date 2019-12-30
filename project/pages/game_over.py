from pages.clear_console import clear_console
from pages.read_key import read_key


def game_over(session):
    clear_console()
    print('TURN: '+str(session.get_turn()))
    print(str(session.get_money()) + '$')
    print()
    print("YOU'VE LOST...")
    read_key()
    session.set_stage('menu')
    return
