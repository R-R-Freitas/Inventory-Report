from collections.abc import Iterator


class InventoryIterator(Iterator):
    def __init__(self, inventory):
        self.inventory = inventory
        self.curr = 0

    def __next__(self):
        try:
            result = self.inventory[self.curr]
        except IndexError:
            raise StopIteration
        self.curr += 1
        return result
