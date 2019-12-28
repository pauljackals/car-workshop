from pages.clear_console import clear_console
from pages.load import load
from pages.menu import menu
from pages.new import new
from pages.game import game
from pages.read_key import read_key
from pages.session import Session


class Main:

    @staticmethod
    def main():
        clear_console()
        session = Session()
        session.set_stage('menu')
        while True:
            stage = session.get_stage()
            if stage == 'menu':
                menu(session)
            elif stage == 'new':
                new(session)
            elif stage == 'quit':
                break
            elif stage == 'game':
                game(session)
            elif stage == 'load':
                if not load(session):
                    print('No save files!')
                    read_key()
                    session.set_stage('menu')


if __name__ == "__main__":
    Main.main()
