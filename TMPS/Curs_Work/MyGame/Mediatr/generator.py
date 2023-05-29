import airplane
import data_planes
import random
import flyinfo_cl
import pandas as pd

#Facade

class Generator:
    def __init__(self):
        self.pd_plane = data_planes.DataP.get_instance()
        self.df_fly = pd.read_csv('../flyinfo_data/city_county.csv')
        self.df_names = pd.read_csv('../flyinfo_data/names_prep.csv')

    def create_airplane(self):
        rn = random.randint(0, len(self.pd_plane.df) - 1)
        name = self.pd_plane.df.iloc[rn]['tailnum'] + ' ' + self.pd_plane.df.iloc[rn]['model']

        factory = airplane.TransportFactory()
        air_builder = factory.create_transport_type('Airplane')
        nr1 = random.randint(0,len(self.df_names)-1)
        nr2 = random.randint(0, len(self.df_names) - 1)
        plane = air_builder.set_image("images/airplanev2.png") \
            .set_scale(0.3) \
            .set_air_type(name) \
            .set_speed(600 + random.randint(-200,200)) \
            .set_name_first_pilot(self.df_names.iloc[nr1]['First Name'] + ' ' + self.df_names.iloc[nr1]['Last Name']) \
            .set_name_second_pilot(self.df_names.iloc[nr2]['First Name'] + ' ' + self.df_names.iloc[nr2]['Last Name']) \
            .get_airplane() \

        plane.center_x = random.randint(100, 900)
        plane.center_y = random.randint(100, 700)
        plane.angle = random.randint(0, 360)

        return plane

    def create_flyinfo(self,plane):

        pass




    #using this when you need to create city_country.csv
    def get_list_of_city(self):
        self.city_and_country = [[],[]]
        with open("../flyinfo_data/worldcities.csv", 'r', encoding='utf-8') as file:
            for line in file.readlines():
                self.city_and_country[0].append(line.split(",")[1].replace("\"", ""))
                self.city_and_country[1].append(line.split(",")[4].replace("\"", ""))
        print(self.city_and_country[0])
        print(self.city_and_country[1])
        with open("../flyinfo_data/city_county.csv", 'w', encoding="utf-8") as file:
            for i in range(len(self.city_and_country[0])):
                file.write(self.city_and_country[0][i] + ","+self.city_and_country[1][i]+'\n')



