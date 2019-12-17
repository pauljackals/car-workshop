from pages.clear_console import clear_console
from pages.menu import menu
from pages.new import new
from pages.game import game


class Main:

    @staticmethod
    def main():
        clear_console()
        stage = 'menu'

        while True:
            if stage == 'menu':
                stage = menu()
            elif stage == 'new':
                stage = game(new=True, data=new())
            elif stage == 'quit':
                break


if __name__ == "__main__":
    Main.main()
