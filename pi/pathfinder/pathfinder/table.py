from shapely import geometry
from shapely.geometry.collection import GeometryCollection


class Table:
    """ represent eurobot game table """
    def __init__(self, dim=(3000.0, 2000.0)):
        self.dim = dim
        self.obstacles = []
        self.robots = []

    def add_rectangle(self, x, y, dx, dy):
        """ add a rectangle to list of obstacles map (obstacle)"""
        self.obstacles.append(geometry.box(x, y, x + dx, y + dy))

    def add_circle(self, x, y, radius):
        pass  # TODO

    def add_big_robot(self, x, y):
        pass

    def check_path(self, list_of_waypoint):
        """ check that the path does not cross anything """
        path = geometry.LineString(list_of_waypoint)
        obstacles_collection = GeometryCollection(self.obstacles + self.robots)
        return not path.crosses(obstacles_collection)
