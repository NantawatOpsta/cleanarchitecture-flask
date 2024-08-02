from entity import promotion


class PromotionUseCase:

    def get_promotions(self):
        return promotion.get_promotions()
