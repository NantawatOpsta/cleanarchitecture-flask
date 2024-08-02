from entity import product, promotion


class ProductUseCase:

    def get_products(self):
        return product.get_products()

    def get_products_with_discount_price(self):
        products = product.get_products()
        promotions = promotion.get_promotions()

        products_with_discount = []
        for discount_promotion in promotions:
            for full_price_product in products:
                if discount_promotion.product_group == full_price_product.group:
                    full_price_product.discount_price = full_price_product.price - \
                        full_price_product.price * \
                        (discount_promotion.discount/100)
                    products_with_discount.append(full_price_product)
        return products_with_discount
