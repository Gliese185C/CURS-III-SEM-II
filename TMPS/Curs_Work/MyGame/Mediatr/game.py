import arcade
from PyQt5 import QtCore, QtGui, QtWidgets
import airplane
#import terminal
import random
import time
from constants import *
import data_planes
import generator
from UI import terminal as tm
import sys
import MainAdapter


airplane_names = []



class Game(arcade.Window):
    __instance = None



    def __init__(self,width,height,title):
        if Game.__instance is not None:
            raise Exception("Do not create the new object, just get existing (get_instance)")
        else:
            super(Game, self).__init__(width,height,title)
            self.bg = arcade.load_texture('images/map.png')
            self.area_planes = arcade.SpriteList()
            self.pd = data_planes.DataP()
            self.generator = generator.Generator()
            self.start_schedule = time.time()
            self.airPortObserver = MainAdapter.Adapter()
            self.setup_terminal()
            self.setup()

    @staticmethod
    def get_instance():
        if Game.__instance is None:
            Game()
        return Game.__instance

    def setup_terminal(self):
        self.app = QtWidgets.QApplication(sys.argv)
        self.MainWindow = QtWidgets.QMainWindow()
        self.ui = tm.Ui_MainWindow()
        self.ui.setupUi(self.MainWindow, self)
        self.MainWindow.show()

    def get_planes(self):
        return self.area_planes
    def setup(self):
        for i in range(19):
            plane = self.generator.create_airplane()
            self.area_planes.append(plane)
            self.airPortObserver.registration(plane)
        self.ui.fill_table(self.area_planes)


    def on_draw(self):
        arcade.draw_texture_rectangle(SCREEN_WIDTH//2,SCREEN_HEIGHT//2,SCREEN_WIDTH,SCREEN_HEIGHT, self.bg)
        self.area_planes.draw()
        for plane in self.area_planes:
            arcade.draw_text(plane.air_type, plane.center_x - len(plane.air_type)*7//2, plane.center_y+15,font_size=10,color=arcade.color.CYAN)

    def update(self, delta_time: float):
        self.area_planes.update()
        if time.time() - self.start_schedule > 1:
            self.start_schedule = time.time()
            self.ui.change_speed(self.area_planes)





window = Game(SCREEN_WIDTH,SCREEN_HEIGHT,"AirportDispatcher")
arcade.run()