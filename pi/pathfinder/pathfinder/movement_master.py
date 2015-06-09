from position import Position


class MovementMaster:
    """ this class controls the movement of the robot: it
    moves a target point every 20 ms. It is capable of changing the
    path to dynamically avoid the other robots on the table """
    def __init__(self):
        self.target = Position()
        self.current = Position()

    def run(self):
        """ call every 20 ms"""
        pass

    def goto_position(self, target):
        """ redefine the destination
            input target : Position object"""
        self.target = target

    def goto_position_speed(self):
        """ target point is a position and a speed """
        pass

    def update_current(self, current):
        self.current = current
