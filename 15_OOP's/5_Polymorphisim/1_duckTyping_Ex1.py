def Driver(car):

    car.drive()


class Creta:

    def drive(self):
        print("Creta is driving")


class Toyota:

    def drive(self):
        print("Toyota is driving")


Toy = Toyota()

Driver(Toy)

# Toyota is driving

print()

cr1 = Creta()
Driver(cr1)

# Creta is driving
