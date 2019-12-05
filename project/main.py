from people.client import Client
from people.mechanic import Mechanic
from vehicles.car import Car

client = Client()
car = Car()
mechanic = Mechanic()

client.set_vehicle(car)
car.set_owner(client)

client.print_info()
print()
mechanic.print_info()
print()
car.print_info()
