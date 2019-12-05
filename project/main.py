import os
import platform

from people.mechanic import Mechanic
from vehicles.car import Car


class Main:

    @staticmethod
    def main():

        if platform.system() == "Windows":
            os.system("cls")
        elif platform.system() == "Linux":
            os.system("clear")

        car = Car()
        client = car.get_owner()
        mechanic = Mechanic()

        car.print_info()
        print()
        client.print_info()
        print()
        mechanic.print_info()


if __name__ == "__main__":
    Main.main()
