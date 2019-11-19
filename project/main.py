from people import skills
from people.client import Client
from people.mechanic import Mechanic
from vehicles.car import Car

client = Client("John", "Doe")
car = Car("XY54343", "blue")
mechanic = Mechanic("Tom", "Kit", skills.levels_of_skill["apprentice"])

client.set_vehicle(car)
car.set_owner(client)

client.print_info()
print()
mechanic.print_info()
print()
car.print_info()
