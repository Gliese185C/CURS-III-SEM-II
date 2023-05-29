import obs


#Adapter

class Adapter():
    def __init__(self):
        self.aerodrom = obs.AirPort("Kilomanjaro")


    def registration(self, plane):
        self.aerodrom.attach(plane)


    def leave(self, plane):
        self.aerodrom.detach(plane)


    def notify(self, names):
        self.aerodrom.notify(names)