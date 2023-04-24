#-------------------------------------------------------------------------------------------
#Facade
'''
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

'''

#-------------------------------------------------------------------------------------------
#Adapter
'''
class Server:

    def getHost(self):
        return ("host/static/78-213-113-153.moldtelecom.md")



class Web:

    def showIp(self,host):
        if len(host) > 16:
            return "Error"
        return host


class Adapter:

    def hostToIp(self,host):
        ip = host
        new = [str(item) for item in range(1,10)]
        for item in host:
            if item not in new and item != "-":
                ip = ip.replace(item, "")
        ip = ip.replace("-",".")

        return ip




if __name__ == "__main__":
    backside = Server()
    frontside = Web()
    adapter = Adapter()

    print(frontside.showIp(adapter.hostToIp(backside.getHost())))


'''
#---------------------------------------------------------------------------------------
#Bridge

'''
class MusicPlayer:
    def __init__(self, implementation):
        self.implementation = implementation

    def play_song(self, song):
        self.implementation.play_song(song)

    def set_volume(self, volume):
        self.implementation.set_volume(volume)


class SpeakerSystem:
    def play_song(self, song):
        print(f"Playing {song} on speakers")

    def set_volume(self, volume):
        print(f"Setting speakers volume to {volume}")


class Headphones:
    def play_song(self, song):
        print(f"Playing {song} on headphones")

    def set_volume(self, volume):
        print(f"Setting headphones volume to {volume}")


speaker_system = SpeakerSystem()
music_player1 = MusicPlayer(speaker_system)
music_player1.play_song("Bohemian Rhapsody")
music_player1.set_volume(10)

headphones = Headphones()
music_player2 = MusicPlayer(headphones)
music_player2.play_song("Stairway to Heaven")
music_player2.set_volume(5)
'''

#-------------------------------------------------------------------------------
#Composite

'''

class ElectricComponent:
    def get_power_consumption(self):
        pass


class PowerPlant(ElectricComponent):
    def __init__(self, power_output):
        self.power_output = power_output

    def get_power_consumption(self):
        return self.power_output


class Substation(ElectricComponent):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def get_power_consumption(self):
        total_power_consumption = 0
        for component in self.components:
            total_power_consumption += component.get_power_consumption()
        return total_power_consumption


class CityElectricity:
    def __init__(self):
        self.all = Substation()

    def load(self):
        substation1 = Substation()
        substation1.add_component(PowerPlant(1000))
        substation1.add_component(PowerPlant(500))
        self.all.add_component(substation1)

        substation2 = Substation()
        substation2.add_component(PowerPlant(1500))
        substation2.add_component(PowerPlant(800))
        substation2.add_component(substation1)
        self.all.add_component(substation2)


    def group_selected(self, components):
        group = Substation()
        for component in components:
            group.add_component(component)
            self.all.remove_component(component)
        self.all.add_component(group)
        print(f"Total power consumption: {self.all.get_power_consumption()} MW")


city_electricity = CityElectricity()
city_electricity.load()
city_electricity.group_selected([city_electricity.all.components[0], city_electricity.all.components[1]])

'''

#--------------------------------------------------------------------------------------------
#Decorator
'''
class Flight:
    def __init__(self, flight_number, destination, departure_time, arrival_time, seats):
        self.flight_number = flight_number
        self.destination = destination
        self.departure_time = departure_time
        self.arrival_time = arrival_time
        self.seats = seats

    def get_flight_details(self):
        return f"Flight {self.flight_number} to {self.destination} departs at {self.departure_time} and arrives at {self.arrival_time}."

    def reserve_seat(self):
        if self.seats > 0:
            self.seats -= 1
            return True
        else:
            return False


class BaggageDecorator:
    def __init__(self, flight, baggage_allowance):
        self.flight = flight
        self.baggage_allowance = baggage_allowance

    def get_flight_details(self):
        return f"{self.flight.get_flight_details()} Baggage allowance: {self.baggage_allowance}."

    def add_baggage(self, weight):
        if weight <= self.baggage_allowance:
            return True
        else:
            return False


class SeatReservationDecorator:
    def __init__(self, flight):
        self.flight = flight

    def get_flight_details(self):
        return self.flight.get_flight_details()

    def reserve_seat(self):
        if self.flight.reserve_seat():
            print("Seat reserved successfully!")
            return True
        else:
            print("No seats available!")
            return False


# Создание объекта Flight
flight1 = Flight("BA123", "London", "10:00", "12:00", 100)

# Создание объекта BaggageDecorator на основе объекта Flight
flight2 = BaggageDecorator(flight1, 30)

# Создание объекта SeatReservationDecorator на основе объекта BaggageDecorator
flight3 = SeatReservationDecorator(flight2)

# Получение информации о рейсе
print(flight3.get_flight_details())

# Резервирование места на борту
flight3.reserve_seat()

# Добавление багажа
if flight2.add_baggage(25):
    print("Baggage added successfully!")
else:
    print("Exceeds baggage allowance!")

'''