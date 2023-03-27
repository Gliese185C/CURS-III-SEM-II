class Order:
    def __init__(self):
        self.shipping_address = None
        self.billing_address = None
        self.products = []
        self.payment_method = None

    def __str__(self):
        shipping_address = f'Shipping Address: {self.shipping_address}\n' if self.shipping_address else ''
        billing_address = f'Billing Address: {self.billing_address}\n' if self.billing_address else ''
        products = '\n'.join([f'- {product}' for product in self.products])
        payment_method = f'Payment Method: {self.payment_method}\n' if self.payment_method else ''

        return f'{shipping_address}{billing_address}Products:\n{products}\n{payment_method}'


class OrderBuilder:
    def __init__(self):
        self.order = Order()

    def set_shipping_address(self, address):
        self.order.shipping_address = address
        return self

    def set_billing_address(self, address):
        self.order.billing_address = address
        return self

    def add_product(self, product):
        self.order.products.append(product)
        return self

    def set_payment_method(self, method):
        self.order.payment_method = method
        return self

    def get_order(self):
        return self.order


builder = OrderBuilder()
order = builder.set_shipping_address('123 Main St') \
               .set_billing_address('456 Market St') \
               .add_product('Apple') \
               .add_product('Banana') \
               .set_payment_method('Credit Card') \
               .get_order()

print(order)

'''
Суть паттерна Builder заключается в разделении процесса создания объекта на отдельные шаги, что позволяет создавать объекты поэтапно и с различными параметрами, не затрагивая при этом его внутреннее устройство.

В результате мы получаем следующие преимущества:

Упрощается процесс создания объектов.
Позволяет создавать объекты пошагово, изменяя при этом их состояние.
Облегчает создание объектов со сложными конфигурациями.
Сокращает дублирование кода при создании объектов.
В нашем примере, мы разбили процесс создания заказа на несколько шагов: добавление адреса доставки, добавление адреса оплаты, добавление товаров и выбор метода оплаты. 
Клиент может вызвать каждый из этих методов отдельно и в нужном порядке, чтобы создать заказ с нужными характеристиками.
'''