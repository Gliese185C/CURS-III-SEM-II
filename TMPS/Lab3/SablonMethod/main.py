from abc import ABC, abstractmethod

class AircraftFactory(ABC):
    """
    Абстрактный класс фабрики по производству самолетов, определяющий шаблонный метод
    для производства самолетов.
    """

    def manufacture_aircraft(self) -> None:
        """
        Шаблонный метод производства самолетов, который состоит из вызова (обычно) абстрактных
        примитивных операций.
        """
        self.assemble_fuselage()
        self.install_engine()
        self.install_wings()
        self.install_avionics()
        self.paint_aircraft()

    # Абстрактные методы, которые должны быть реализованы в подклассах.

    @abstractmethod
    def assemble_fuselage(self) -> None:
        pass

    @abstractmethod
    def install_engine(self) -> None:
        pass

    @abstractmethod
    def install_wings(self) -> None:
        pass

    @abstractmethod
    def install_avionics(self) -> None:
        pass

    # Методы с реализацией по умолчанию, которые могут быть переопределены в подклассах.

    def paint_aircraft(self) -> None:
        print("Painting the aircraft.")

    def test_flight(self) -> None:
        print("Conducting a test flight.")

class BoeingFactory(AircraftFactory):
    """
    Конкретная фабрика для производства самолетов Boeing.
    """

    def assemble_fuselage(self) -> None:
        print("Assembling the Boeing fuselage.")

    def install_engine(self) -> None:
        print("Installing the Boeing engine.")

    def install_wings(self) -> None:
        print("Installing the Boeing wings.")

    def install_avionics(self) -> None:
        print("Installing the Boeing avionics.")

class AirbusFactory(AircraftFactory):
    """
    Конкретная фабрика для производства самолетов Airbus.
    """

    def assemble_fuselage(self) -> None:
        print("Assembling the Airbus fuselage.")

    def install_engine(self) -> None:
        print("Installing the Airbus engine.")

    def install_wings(self) -> None:
        print("Installing the Airbus wings.")

    def install_avionics(self) -> None:
        print("Installing the Airbus avionics.")

    def paint_aircraft(self) -> None:
        print("Applying the Airbus livery paint job.")

if __name__ == "__main__":
    # Пример использования шаблонного метода для производства самолетов Boeing.
    print("Producing a Boeing aircraft:")
    boeing_factory = BoeingFactory()
    boeing_factory.manufacture_aircraft()
    print("")

    # Пример использования шаблонного метода для производства самолетов Airbus.
    print("Producing an Airbus aircraft:")
    airbus_factory = AirbusFactory()
    airbus_factory.manufacture_aircraft()
    print("")
