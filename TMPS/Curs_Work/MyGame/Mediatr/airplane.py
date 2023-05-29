import time
import copy
import arcade
import math
from constants import *
import random
from abc import ABC, abstractmethod
from datetime import datetime, timedelta

#Prototype line 82
#Builder
#FactoryMethod
#SablonMethod



class TransportBuilder(ABC):
    @abstractmethod
    def info_about_Builder(self, type):
        print("This is Transport Builder")


class TransportFactory:
    @staticmethod
    def create_transport_type(type: str) -> TransportBuilder:
        if type == 'Airplane':
            return AirplaneBuilder()
        elif type == 'Car':
            pass
        elif type == 'Train':
            pass
        else:
            raise ValueError(f"Unsupported document format type: {type}")





def rotation(plane):
    distance = 10



    if plane.center_x + distance >= SCREEN_WIDTH:
        if plane.start_hide == 0:
            plane.start_hide = time.time()
        if time.time() - plane.start_hide > 15 and not plane.was_hidden:
            plane.was_hidden = True
            plane.angle = random.randint(90,270)
            plane.center_y = random.randint(50,750)



    elif plane.center_x - distance <= 0:

        if plane.start_hide == 0:
            plane.start_hide = time.time()
        if time.time() - plane.start_hide > 15 and not plane.was_hidden:
            plane.was_hidden = True
            plane.angle = random.randint(-80,80)
            plane.center_y = random.randint(50, 750)

    elif plane.center_y - distance <= 0:

        if plane.start_hide == 0:
            plane.start_hide = time.time()
        if time.time() - plane.start_hide > 7 and not plane.was_hidden:
            plane.was_hidden = True
            plane.angle = random.randint(10,170)
            plane.center_x = random.randint(100,900)

    elif plane.center_y + distance >= SCREEN_HEIGHT:
        if plane.start_hide == 0:
            plane.start_hide = time.time()
        if time.time() - plane.start_hide > 7 and not plane.was_hidden:
            plane.was_hidden = True
            plane.angle = random.randint(190,350)
            plane.center_x = random.randint(100, 900)


    else:
        plane.rotation = 0
        plane.speed_rotation = 0
        plane.start_hide = 0
        plane.was_hidden = False


class Airplane(arcade.Sprite):

    def __init__(self):
        super().__init__()
        self.air_type = None
        self.rotation = 0
        self.state_rotation = False
        self.random_angle = 0
        self.speed = None
        self.last_position_x = self.center_x
        self.last_position_y = self.center_y
        self.start_hide = 0
        self.was_hidden = False
        self.first_pilot = ""
        self.second_pilot = ""
        self.status = None
        self.set_status()

    def set_status(self):
        if random.randint(1,10) in range(1,3):
            self.status = False
        else:
            self.status = True

    def get_info(self):
        info = ""
        info = f"Type: {self.air_type}\nLast speed: {self.speed}\n" \
               f"First pilot: {self.first_pilot}\nSecond pilot: {self.second_pilot}"

        with open('data_log.txt', 'a', encoding='utf-8') as log:
            log.write(f"\n[{datetime.now()}] Были получены следующие данные борта {self.air_type}:\n{info}")
        return info


    def landing(self,air_names):
        with open('data_log.txt', 'a', encoding='utf-8') as log:
            log.write(f"\n[{datetime.now()}] Борт {self.air_type} принял уведомление о посадке рейсов:")

    def clone(self):
        return copy.deepcopy(self)

    def update(self):
        angle = self.angle
        '''
        if self.state_rotation:
            self.speed = 10
        else:
            self.speed = 7
        '''
        move_x = math.cos(math.radians(angle)) / (self.speed/125)
        move_y = math.sin(math.radians(angle)) / (self.speed/125)
        self.center_x += move_x
        self.center_y += move_y

        rotation(self)





class AirplaneBuilder(TransportBuilder):

    def __init__(self):
        self.plane = Airplane()

    def set_image(self,image):
        self.plane.texture = arcade.load_texture(image)
        return self

    def set_scale(self,scale):
        self.plane.scale = scale
        return self

    def set_air_type(self,air_type):
        self.plane.air_type = air_type
        return self

    def set_speed(self,speed):
        self.plane.speed = speed
        return self

    def set_name_first_pilot(self,name):
        self.plane.first_pilot = name
        return self

    def set_name_second_pilot(self,name):
        self.plane.second_pilot = name
        return self


    def info_about_Builder(self, type):
        print("This is Airplane Builder")

    def get_airplane(self):
        return self.plane







