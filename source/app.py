from flask import Flask
from usecase.promotion import PromotionUseCase
from usecase.product import ProductUseCase

app = Flask(__name__)


@app.route('/')
def healthcheck():
    return 'ok'


@app.route('/promotion')
def promotion():
    promotion_usecase = PromotionUseCase()
    promotions = promotion_usecase.get_promotions()

    promotion_json = []
    for promotion in promotions:
        promotion_json.append({
            'promotion_id': promotion.promotion_id,
            'name': promotion.name,
            'description': promotion.description,
            'discount': promotion.discount,
            'product_group': promotion.product_group
        })
    return {'promotions': promotion_json}


@app.route('/product')
def product():
    product_usecase = ProductUseCase()
    products = product_usecase.get_products()

    product_json = []
    for product in products:
        product_json.append({
            'product_id': product.product_id,
            'name': product.name,
            'price': product.price,
            'group': product.group
        })

    return {'products': product_json}


@app.route('/product/discount')
def product_discount():
    product_usecase = ProductUseCase()
    products = product_usecase.get_products_with_discount_price()

    product_json = []
    for product in products:
        product_json.append({
            'product_id': product.product_id,
            'name': product.name,
            'price': product.price,
            'group': product.group,
            'discount_price': product.discount_price
        })
    return {'products': product_json}


if __name__ == "__main__":
    app.run(debug=True)
