from people.Client import Client
from vehicles.Car import Car

client = Client("John", "Doe")
car = Car("XY54343")

client.set_vehicle(car)
car.set_owner(client)
