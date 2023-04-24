from abc import ABC, abstractmethod
from typing import List


class Subject(ABC):
    """
    Интерфейс Наблюдаемого объекта определяет методы для добавления и удаления
    наблюдателей.
    """
    @abstractmethod
    def attach(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def detach(self, observer: 'Observer') -> None:
        pass

    @abstractmethod
    def notify(self) -> None:
        pass


class Port(Subject):
    """
    Класс Порт представляет объект, за которым наблюдают наблюдатели.
    """
    def __init__(self, name: str) -> None:
        self.name = name
        self.ships = []  # текущее расписание кораблей
        self.observers: List[Observer] = []

    def attach(self, observer: 'Observer') -> None:
        print(f"{observer.name} подписался на обновления порта {self.name}")
        self.observers.append(observer)

    def detach(self, observer: 'Observer') -> None:
        print(f"{observer.name} отписался от обновлений порта {self.name}")
        self.observers.remove(observer)

    def notify(self) -> None:
        print(f"\nПорт {self.name} оповещает всех наблюдателей о новом расписании:")
        for observer in self.observers:
            observer.update(self.ships)

    def update_schedule(self, new_schedule: List[str]) -> None:
        print(f"\nОбновление расписания в порту {self.name}")
        self.ships = new_schedule
        self.notify()


class Observer(ABC):
    """
    Интерфейс Наблюдателя определяет метод обновления, который вызывается
    наблюдаемым объектом для оповещения наблюдателя о новых данных.
    """
    @abstractmethod
    def update(self, ships: List[str]) -> None:
        pass


class CargoShip(Observer):
    """
    Класс Грузового корабля представляет объект, который наблюдает за портом и
    реагирует на изменения в расписании.
    """
    def __init__(self, name: str, port: Port) -> None:
        self.name = name
        self.port = port
        self.port.attach(self)

    def update(self, ships: List[str]) -> None:
        print(f"\n{self.name} получил новое расписание:")
        for ship in ships:
            print(f" - {ship}")

    def leave_port(self) -> None:
        self.port.detach(self)


if __name__ == '__main__':
    # Создаем порты
    port1 = Port("Рио-де-Жанейро")
    port2 = Port("Санкт-Петербург")

    # Создаем грузовые корабли, наблюдающие за портами
    ship1 = CargoShip("Корабль 1", port1)
    ship2 = CargoShip("Корабль 2", port2)
    ship3 = CargoShip("Корабль 3", port1)

    # Обновляем расписание в порту 1
    port1.update_schedule(["Корабль А", "Корабль Б", "Корабль В"])

    # Грузовой корабль 1 отписывается от порта 1
    ship1.leave_port()

    # Обновляем расписание в порту 1
    port1.update_schedule(["Корабль Г", "Корабль Д", "Корабль Е", "Корабль Ж"])

    # Грузовой корабль 2 отписывается от порта 2
    ship2.leave_port()

    # Обновляем расписание в порту 2
    port2.update_schedule(["Корабль К", "Корабль Л", "Корабль М"])

    # Грузовой корабль 3 отписывается от порта 1
    ship3.leave_port()

    # Обновляем расписание в порту 1
    port1.update_schedule(["Корабль Н", "Корабль О", "Корабль П"])
