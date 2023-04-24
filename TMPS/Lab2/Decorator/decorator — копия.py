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
