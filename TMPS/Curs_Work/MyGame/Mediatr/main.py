from __future__ import annotations
from abc import ABC


class Mediator(ABC):
    """
    Интерфейс Посредника предоставляет метод, используемый компонентами для
    уведомления посредника о различных событиях. Посредник может реагировать на
    эти события и передавать исполнение другим компонентам.
    """

    def notify(self, sender: object, event: str) -> None:
        pass


class AirportDispatcher(Mediator):
    def __init__(self):
        self._runway_available = True
        self._aircrafts_waiting = []

    def request_runway(self, aircraft: Aircraft) -> bool:
        if self._runway_available:
            self._runway_available = False
            print(f"Runway granted to {aircraft.name}")
            return True
        else:
            print(f"Runway not available, {aircraft.name} is added to queue")
            self._aircrafts_waiting.append(aircraft)
            return False

    def release_runway(self, aircraft: Aircraft):
        if self._aircrafts_waiting and not self._runway_available and aircraft == self._aircrafts_waiting[0]:
            aircraft = self._aircrafts_waiting.pop(0)
            self.request_runway(aircraft)
            self._runway_available = True

    def notify(self, sender: object, event: str) -> None:
        if isinstance(sender, Aircraft):
            if event == "request_runway":
                self.request_runway(sender)
            elif event == "release_runway":
                self.release_runway(sender)


class Aircraft:
    def __init__(self, name: str, dispatcher: AirportDispatcher):
        self._name = name
        self._dispatcher = dispatcher

    @property
    def name(self):
        return self._name

    def request_runway(self):
        self._dispatcher.notify(self, "request_runway")

    def release_runway(self):
        self._dispatcher.notify(self, "release_runway")


if __name__ == "__main__":
    dispatcher = AirportDispatcher()

    aircraft1 = Aircraft("Boeing 737", dispatcher)
    aircraft2 = Aircraft("Airbus A320", dispatcher)
    aircraft3 = Aircraft("Embraer E190", dispatcher)

    aircraft1.request_runway()
    aircraft2.request_runway()
    aircraft3.release_runway()
