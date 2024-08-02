class Product:

    product_id = None
    name = None
    price = None
    quantity = None
    group = None

    def __init__(self, product_id, name, price, quantity, group):
        self.product_id = product_id
        self.name = name
        self.price = price
        self.quantity = quantity
        self.group = group


products = [
    Product(1, 'Apple', 0.50, 100, 'Fruit'),
    Product(2, 'Banana', 0.30, 200, 'Fruit'),
    Product(3, 'Orange', 0.40, 150, 'Fruit'),
    Product(4, 'Carrot', 0.60, 100, 'Vegetable'),
    Product(5, 'Potato', 0.40, 200, 'Vegetable'),
    Product(6, 'Onion', 0.50, 150, 'Vegetable')
]


def get_products():
    return products
