import time

import arcade
import random

#Decorator
from datetime import datetime, timedelta
class FlightInfo:

    def __init__(self, plane):
        self.plane = plane
        self.departure_date = None
        self.departure_city = None
        self.city_of_arrival = None
        self.number_of_passengers = None
        self.first_pilot = None
        self.second_pilot = None


    def get_info(self):

        info = f"Type: {self.plane.air_type}\n" \
               f"Dep date: {self.departure_date}\n" \
               f"Dep city: {self.departure_city}\n" \
               f"Ariv city: {self.city_of_arrival}\n" \
               f"Num of passag: {self.number_of_passengers}\n" \
               f"First pilot: {self.first_pilot}\n" \
               f"Second pilot: {self.second_pilot}"

        with open('data_log.txt', 'a', encoding='utf-8') as log:
            log.write(f"\n[{datetime.now()}] Были получены следующие данные текущего рейса борта {self.plane.air_type}:\n{info}")

        return info







class FlightInfoBuilder:
    def __init__(self,plane):
        self.flightInfo = FlightInfo(plane)

    def set_dep_date(self,departure_date):
        self.flightInfo.departure_date = departure_date
        return self.flightInfo
 
    def set_dep_city(self, departure_city):
        self.flightInfo.departure_city = departure_city
        return self.flightInfo

    def set_city_arrival(self, city_of_arrival):
        self.flightInfo.city_of_arrival = city_of_arrival
        return self.flightInfo

    def set_num_of_pass(self, number_of_passengers):
        self.flightInfo.number_of_passengers = number_of_passengers
        return self.flightInfo

    def set_first_pilot(self, first_pilot):
        self.flightInfo.first_pilot = first_pilot
        return self.flightInfo

    def set_second_pilot(self, second_pilot):
        self.flightInfo.second_pilot = second_pilot
        return self.flightInfo

    def get_flighInfo(self):
        return self.flightInfo