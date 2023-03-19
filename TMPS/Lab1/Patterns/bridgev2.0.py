# Абстрактный класс Abstraction, который определяет интерфейс для взаимодействия с устройствами
class Abstraction:
    def __init__(self, implementation):
        self.implementation = implementation

    def turn_on(self):
        self.implementation.turn_on()

    def turn_off(self):
        self.implementation.turn_off()

    def set_brightness(self, brightness):
        self.implementation.set_brightness(brightness)

# Класс Implementation, который определяет основные функции устройств
class Implementation:
    def turn_on(self):
        pass

    def turn_off(self):
        pass

    def set_brightness(self, brightness):
        pass

# Конкретная реализация Implementation1, которая управляет умными лампами
class Implementation1(Implementation):
    def turn_on(self):
        print("Smart lamp turned on")

    def turn_off(self):
        print("Smart lamp turned off")

    def set_brightness(self, brightness):
        print("Smart lamp brightness set to", brightness)

# Конкретная реализация Implementation2, которая управляет обычными лампами
class Implementation2(Implementation):
    def turn_on(self):
        print("Regular lamp turned on")

    def turn_off(self):
        print("Regular lamp turned off")

    def set_brightness(self, brightness):
        print("Regular lamp brightness set to", brightness)

# Конкретная реализация Abstraction1, которая управляет умными лампами в гостиной
class Abstraction1(Abstraction):
    def __init__(self):
        super().__init__(Implementation1())

# Конкретная реализация Abstraction2, которая управляет обычными лампами на кухне
class Abstraction2(Abstraction):
    def __init__(self):
        super().__init__(Implementation2())