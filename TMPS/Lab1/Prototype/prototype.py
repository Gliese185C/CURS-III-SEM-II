import copy

class Prototype:
    def clone(self):
        return copy.deepcopy(self)

class Graphic(Prototype):
    def __init__(self, x, y, color):
        self.x = x
        self.y = y
        self.color = color

class Rectangle(Graphic):
    def __init__(self, x, y, width, height, color):
        super().__init__(x, y, color)
        self.width = width
        self.height = height

    def clone(self):
        return copy.deepcopy(self)

class Circle(Graphic):
    def __init__(self, x, y, radius, color):
        super().__init__(x, y, color)
        self.radius = radius

    def clone(self):
        return copy.deepcopy(self)


if __name__ == '__main__':
    # Создаем прототипы объектов
    rect_prototype = Rectangle(0, 0, 100, 50, 'blue')
    circle_prototype = Circle(0, 0, 25, 'red')

    # Клонируем объекты и изменяем их свойства
    rect1 = rect_prototype.clone()
    rect1.x = 10
    rect1.y = 20

    circle1 = circle_prototype.clone()
    circle1.x = 30
    circle1.y = 40

    # Проверяем, что объекты созданы корректно
    print(rect_prototype.x,rect_prototype.y,rect_prototype.width,rect_prototype.height,rect_prototype.color)
    print(rect1.x, rect1.y, rect1.width, rect1.height, rect1.color)
    print(circle_prototype.x, circle_prototype.y, circle_prototype.radius, rect_prototype.color)
    print(circle1.x, circle1.y, circle1.radius, circle1.color)


'''
Суть паттерна Прототип (Prototype) заключается в создании объекта через клонирование существующего объекта вместо создания объекта путем вызова конструктора.

То есть, вместо того чтобы создавать новый объект с помощью конструктора и задавать ему начальное состояние, мы создаем копию уже существующего объекта, который уже имеет нужное состояние.

Это позволяет избежать сложной логики создания объектов и упростить создание объектов, особенно если объекты довольно сложны и имеют множество свойств и методов.

В Python реализация паттерна Прототип достаточно проста, так как Python имеет встроенную поддержку клонирования объектов через метод copy().

В этом примере мы создали два класса Rectangle и Circle, которые наследуются от базового класса Graphic, который в свою очередь наследуется от Prototype. Классы Rectangle и Circle реализуют метод clone, создающий копию объекта с помощью глубокого копирования.

Затем мы создаем прототипы объектов Rectangle и Circle и клонируем их, чтобы получить новые объекты. В конце мы проверяем, что новые объекты были созданы корректно, изменив значения их свойств.
'''

