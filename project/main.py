from pages.clear_console import clear_console
from pages.menu import menu


class Main:

    @staticmethod
    def main():

        clear_console()
        menu()


if __name__ == "__main__":
    Main.main()
