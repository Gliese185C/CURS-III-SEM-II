class Sport:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @staticmethod
    def create(*args,**kwargs):
        return Sport(*args,**kwargs)


class Suv:
    def __init__(self,name,price):
        self.name = name
        self.price = price

    @staticmethod
    def create(*args,**kwargs):
        return Suv(*args,**kwargs)

class ProductFactory:
    @staticmethod
    def create_product(product_type, *args, **kwargs):
        products = {
            'Sport': Sport.create,
            'Suv': Suv.create,
        }
        create_func = products.get(product_type)
        if create_func is not None:
            return create_func(*args, **kwargs)
        else:
            return None

if __name__ == "__main__":

    tmp = ProductFactory()
    car = tmp.create_product("Sport","Lambo",123)
    print(car.name)