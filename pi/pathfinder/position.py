import math


class Position:
    """ describe a position of a robot on the table"""
    def __init__(self, x=0, y=0, cap=0):
        self.x = x
        self.y = y
        self.cap = cap

    def translation_forward(self, d):
        """ make a translation forward (defined by the cap) """
        self.x += math.cos(self.cap) * d
        self.x += math.sin(self.cap) * d
