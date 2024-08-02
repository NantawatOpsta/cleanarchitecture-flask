class Promotion:

    promotion_id = None
    name = None
    description = None
    discount = None
    product_group = None

    def __init__(self, promotion_id, name, description, discount, product_group):
        self.promotion_id = promotion_id
        self.name = name
        self.description = description
        self.discount = discount
        self.product_group = product_group


promotions = [
    Promotion(1, 'Fruit Discount', 'Fruit 10% off', 10, 'Fruit'),
    Promotion(2, 'Vegetable Discount', 'Vegetable 20% off', 20, 'Vegetable')
]


def get_promotions():
    return promotions
