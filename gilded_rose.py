# -*- coding: utf-8 -*-

class GildedRose(object):

    def __init__(self, items):
        self.items = items

    def update_quality(self):
        for item in self.items:
            item.update()


class ItemFactory:

    @staticmethod
    def create_item(name: str, quality: int, sell_in: int):
        if name == "Aged Brie":
            return AgedBrie(name, sell_in, quality)
        elif name == "Sulfuras":
            return Sulfuras(name, sell_in, quality)
        elif name == "Backstage passes":
            return BackStagePass(name, sell_in, quality)
        
        return Item(name, sell_in, quality)


class Item:
    def __init__(self, name, sell_in, quality):
        self.name = name
        self.sell_in = sell_in
        self.quality = quality

    def __repr__(self):
        return "%s, %s, %s" % (self.name, self.sell_in, self.quality)

    def update(self):
        if self.quality <= 0:
            return

        if self.quality < 2 and self.sell_in > 0:
            self.quality = 0
            return

        if self.sell_in > 0:
            self.quality = self.quality - 1
        else:
            self.quality = self.quality - 2


class AgedBrie(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        if self.quality < 50:
            self.quality = self.quality + 1


class Sulfuras(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        pass


class BackStagePass(Item):

    def __init__(self, name, sell_in, quality):
        super().__init__(name, sell_in, quality)

    def update(self):
        if 5 < self.sell_in <= 10:
            self.quality = self.quality + 2
        elif 0 < self.sell_in <= 5:
            self.quality = self.quality + 3
        elif self.sell_in <= 0:
            self.quality = 0
        else:
            self.quality = self.quality + 1
