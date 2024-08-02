import unittest
from promotion import PromotionUseCase


class PromotionUseCaseTest(unittest.TestCase):

    def test_get_promotions(self):
        promotion_use_case = PromotionUseCase()
        # get promotion will return 2 list of promotions 
        promotions = promotion_use_case.get_promotions()
        self.assertEqual(len(promotions), 2)
