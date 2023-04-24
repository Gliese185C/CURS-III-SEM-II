class Wheel:
    def install_wheel(self):
        print("The wheel has been installed")

class Electrics:
    def install_electrics(self):
        print("The electrics were carried out")

class SteeringWheel:
    def install_steering_wheel(self):
        print("The steering wheel has been installed")

class Glass:
    def __init__(self):
        self.is_clean = False

    def install_glass(self):
        print("The glass was fixed")

    def clean_glass(self):
        print("The glass is now clean")
        self.is_clean = True

class Seat:
    def __init__(self):
        self.is_clean = False

    def install_seat(self):
        print("The seat has been installed")

    def clean_seat(self):
        print("The seat is now clean")
        self.is_clean = True

class Motor:
    def install_motor(self):
        print("The motor has been installed")

class Facade:
    def __init__(self):
        self.wheel = Wheel()
        self.glass = Glass()
        self.seat = Seat()
        self.motor = Motor()

    def create_car(self):
        for i in range(4):
            wheel = Wheel()
            wheel.install_wheel()

        electrics = Electrics()
        electrics.install_electrics()

        steering_wheel = SteeringWheel()
        steering_wheel.install_steering_wheel()

        for i in range(6):
            glass = Glass()
            glass.install_glass()

        for i in range(5):
            seat = Seat()
            seat.install_seat()

        motor = Motor()
        motor.install_motor()

    def wash_car(self):
        self.glass.clean_glass()
        self.seat.clean_seat()

    def move(self):
        if hasattr(self, 'motor'):
            print("The car is moving")
        else:
            print("The car has not been created yet")

if __name__ == "__main__":
    facade = Facade()
    facade.create_car()
    facade.wash_car()
    facade.move()
