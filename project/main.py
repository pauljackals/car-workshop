from pages.clear_console import clear_console
from pages.menu import menu
from people.client import Client
from people.mechanic import Mechanic
from vehicles.car import Car


class Main:

    @staticmethod
    def main():

        clear_console()
        menu()

        # car = Car()
        # client = Client()
        # car.set_owner(client)
        # client.set_vehicle(car)
        # mechanic = Mechanic()
        #
        # car.print_info()
        # print()
        # client.print_info()
        # print()
        # mechanic.print_info()


if __name__ == "__main__":
    Main.main()
