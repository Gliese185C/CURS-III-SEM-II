from abc import ABC, abstractmethod


class Mediator(ABC):
    @abstractmethod
    def notify(self, sender, event):
        pass


class BuildingMediator(Mediator):
    def __init__(self):
        self.electrician = None
        self.plumber = None
        self.painter = None

    def notify(self, sender, event):
        if event == "electrician_finished":
            self.plumber.do_plumbing()
        elif event == "plumber_finished":
            self.painter.do_painting()
        elif event == "painter_finished":
            print("Building completed!")

    def set_electrician(self, electrician):
        self.electrician = electrician

    def set_plumber(self, plumber):
        self.plumber = plumber

    def set_painter(self, painter):
        self.painter = painter


class BuildingTeamMember:
    def __init__(self, mediator):
        self.mediator = mediator


class Electrician(BuildingTeamMember):
    def do_electrical_work(self):
        print("Electrician finished his work.")
        self.mediator.notify(self, "electrician_finished")


class Plumber(BuildingTeamMember):
    def do_plumbing(self):
        print("Plumber finished his work.")
        self.mediator.notify(self, "plumber_finished")


class Painter(BuildingTeamMember):
    def do_painting(self):
        print("Painter finished his work.")
        self.mediator.notify(self, "painter_finished")


if __name__ == "__main__":
    # Клиентский код.
    mediator = BuildingMediator()
    electrician = Electrician(mediator)
    plumber = Plumber(mediator)
    painter = Painter(mediator)

    mediator.set_electrician(electrician)
    mediator.set_plumber(plumber)
    mediator.set_painter(painter)

    electrician.do_electrical_work()
