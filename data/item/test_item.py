from machine.item import *


class TestItem(MetaItem):
    """
    primitive item for testing purposes
    """
    __id = 1

    def __init__(self, location, x, y):
        MetaItem.__init__(self, location, x, y)
        #assign unique id
        self.id = TestItem.__id
        TestItem.__id += 1

