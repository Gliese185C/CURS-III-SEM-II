
class Wheel:

    def insatllWheel(self):
        print("The wheel has been installed")

class Electrics:

    def installElectrics(self):
        print("The electrics were carried out")

class SteeringWheel:

    def insatllSteeringWheel(self):
        print("The steering wheel has been installed")


class Glass:

    def installGlass(self):
        print("The glass was fixed")

class Seat:

    def installSeat(self):
        print("The seat has been installed")

class Motor:

    def installMotor(self):
        print("The motor has been installed")


class Facade:

    def create_car(self):
        for i in range(4):
            wheel = Wheel()
            wheel.insatllWheel()

        electrics = Electrics()
        electrics.installElectrics()

        steeringWheel = SteeringWheel()
        steeringWheel.insatllSteeringWheel()

        for i in range(6):
            glass = Glass()
            glass.installGlass()

        for i in range(5):
            seat = Seat()
            seat.installSeat()

        motor = Motor()
        motor.installMotor()



if __name__ == "__main__":

    facade = Facade()
    facade.create_car()