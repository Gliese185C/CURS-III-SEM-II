# Общий интерфейс компонентов.
class ElectricComponent:
    def get_power_consumption(self):
        pass

# Простой компонент.
class PowerPlant(ElectricComponent):
    def __init__(self, power_output):
        self.power_output = power_output

    def get_power_consumption(self):
        return self.power_output

# Компоненты могут расширять другие компоненты.
class Substation(ElectricComponent):
    def __init__(self):
        self.components = []

    def add_component(self, component):
        self.components.append(component)

    def remove_component(self, component):
        self.components.remove(component)

    def get_power_consumption(self):
        total_power_consumption = 0
        for component in self.components:
            total_power_consumption += component.get_power_consumption()
        return total_power_consumption

# Приложение работает единообразно как с единичными
# компонентами, так и с целыми группами компонентов.
class CityElectricity:
    def __init__(self):
        self.all = Substation()

    def load(self):
        substation1 = Substation()
        substation1.add_component(PowerPlant(1000))
        substation1.add_component(PowerPlant(500))
        self.all.add_component(substation1)

        substation2 = Substation()
        substation2.add_component(PowerPlant(1500))
        substation2.add_component(PowerPlant(800))
        substation2.add_component(substation1)
        self.all.add_component(substation2)

    # Группировка выбранных компонентов в один сложный
    # компонент.
    def group_selected(self, components):
        group = Substation()
        for component in components:
            group.add_component(component)
            self.all.remove_component(component)
        self.all.add_component(group)
        # Все компоненты будут отрисованы.
        print(f"Total power consumption: {self.all.get_power_consumption()} MW")

# Пример использования
city_electricity = CityElectricity()
city_electricity.load()
city_electricity.group_selected([city_electricity.all.components[0], city_electricity.all.components[1]])
