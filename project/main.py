from people.mechanic import Mechanic
from vehicles.car import Car

car = Car()
client = car.get_owner()
mechanic = Mechanic()

car.print_info()
print()
client.print_info()
print()
mechanic.print_info()
