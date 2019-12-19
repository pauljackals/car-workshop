from pages.clear_console import clear_console
from pages.menu import menu
from pages.new import new
from pages.game import game
from pages.session import Session


class Main:

    @staticmethod
    def main():
        clear_console()
        session = Session()
        # stage = 'menu'
        #
        # while True:
        #     if stage == 'menu':
        #         stage = menu()
        #     elif stage == 'new':
        #         stage = game(new=True, data=new())
        #     elif stage == 'quit':
        #         break
        while True:
            if session.get_stage() == 'menu':
                menu(session)
            elif session.get_stage() == 'new':
                # stage = game(new=True, data=new())
                new(session)
                game(session)
                session = Session()
            elif session.get_stage() == 'quit':
                break


if __name__ == "__main__":
    Main.main()
