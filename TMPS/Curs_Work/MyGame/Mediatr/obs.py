from abc import ABC, abstractmethod
from typing import List
import airplane
from datetime import datetime, timedelta



#Observer
class Subject(ABC):
    """
    Интерфейс Наблюдаемого объекта определяет методы для добавления и удаления
    наблюдателей.
    """
    @abstractmethod
    def attach(self, observer: 'airplane.Airplane') -> None:
        pass

    @abstractmethod
    def detach(self, observer: 'airplane.Airplane') -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class AirPort(Subject):
    __instance = None

    def __init__(self, name: str) -> None:
        if AirPort.__instance is not None:
            raise Exception("Do not create the new object, just get existing (get_instance)")
        else:
            AirPort.__instance = self
            self.name = name
            self.observers: List[airplane.Airplane] = []

    def attach(self, observer: 'airplane.Airplane') -> None:
        print(f"{observer.air_type} зашёл в зону аэродрома {self.name}")
        self.observers.append(observer)
        with open('data_log.txt','a',encoding='utf-8') as log:
            log.write(f"\n[{datetime.now()}] {observer.air_type} зашёл в зону аэродрома {self.name}")

    def detach(self, observer: 'airplane.Airplane') -> None:
        print(f"{observer.air_type} покинул зону аэродрома {self.name}")
        self.observers.remove(observer)
        with open('data_log.txt','a',encoding='utf-8') as log:
            log.write(f"\n[{datetime.now()}] {observer.air_type} покинул зону аэродрома {self.name}")

    def notify(self,air_names) -> None:
        print(f"\nАэродром {self.name} оповещает всех пилотов о посадке рейсов:")
        with open('data_log.txt','a',encoding='utf-8') as log:
            log.write(f"\n[{datetime.now()}] Аэродром {self.name} оповещает всех пилотов о посадке рейсов:")
        for observer in self.observers:
            observer.landing(air_names)


    def process_landing(self):
        pass

    @staticmethod
    def get_instance():
        if AirPort.__instance is None:
            AirPort(Subject)
        return AirPort.__instance