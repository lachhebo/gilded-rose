# -*- coding: utf-8 -*-
import unittest

from gilded_rose import GildedRose, ItemFactory



class GildedRoseTest(unittest.TestCase):

    def test_quality_degrade_twice_as_fast_when_sell_date_inferior_to_O(self):
        # given
        item = ItemFactory.create_item("foo", sell_in=0, quality=4)
        expected_quality = 2
        gilded_rose = GildedRose([item])

        # when
        gilded_rose.update_quality()

        # then
        self.assertEquals(item.quality, expected_quality)

    def test_quality_always_superior_to_O(self):
        # given
        item = ItemFactory.create_item("foo", sell_in=0, quality=0)
        gilded_rose = GildedRose([item])

        # when
        gilded_rose.update_quality()

        # then
        self.assertGreaterEqual(item.quality, 0)

    def test_aged_bried_increase_quality_as_day_pass(self):
        # given
        item = ItemFactory.create_item("Aged Brie", sell_in=3, quality=5)
        gilded_rose = GildedRose([item])

        # when
        gilded_rose.update_quality()

        # then
        assert item.quality == 6
    
    def test_item_quality_lower_50(self):
        # given
        item = ItemFactory.create_item("Aged Brie", sell_in=3, quality=50)
        gilded_rose = GildedRose([item])

        # when
        gilded_rose.update_quality()

        # then
        self.assertLessEqual(item.quality, 50)

    def test_sulfuras_never_decrease_in_quality(self):
        # given
        item = ItemFactory.create_item("Sulfuras", sell_in=1, quality=10)
        gilded_rose = GildedRose([item])

        # when
        gilded_rose.update_quality()

        # then
        assert item.quality == 10

    def test_backstage_quality_increase_by_2_when_sellin_lower_or_equal_10(self):
        # given
        item1 = ItemFactory.create_item("Backstage passes", sell_in=10, quality=10)
        item2 = ItemFactory.create_item("Backstage passes", sell_in=8, quality=10)
        gilded_rose = GildedRose([item1, item2])

        # when
        gilded_rose.update_quality()

        # then
        assert item1.quality == 12
        assert item2.quality == 12

    def test_backstage_quality_increase_by_3_when_sellin_lower_or_equal_5(self):
        # given
        item1 = ItemFactory.create_item("Backstage passes", sell_in=5, quality=10)
        item2 = ItemFactory.create_item("Backstage passes", sell_in=3, quality=10)
        gilded_rose = GildedRose([item1, item2])

        # when
        gilded_rose.update_quality()

        # then
        assert item1.quality == 13
        assert item2.quality == 13
    
    def test_backstage_quality_is_0_when_sellin_is_passed(self):
        item1 = ItemFactory.create_item("Backstage passes", sell_in=0, quality=10)
        item2 = ItemFactory.create_item("Backstage passes", sell_in=-1, quality=10)

        gilded_rose = GildedRose([item1, item2])

        # when
        gilded_rose.update_quality()

        # then
        assert item1.quality == 0
        assert item2.quality == 0


if __name__ == '__main__':
    unittest.main()
