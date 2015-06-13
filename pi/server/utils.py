import json


class Memory():
    def __init__(self):
        self.big_robot = dict(x=0, y=1000, cap=50)
        self.small_robot = dict(x=500, y=500, cap=0)
        self.other_robots = [dict(x=900, y=1000, cap=180)]

    def to_json(self):
        return json.dumps(dict(
            big_robot=self.big_robot,
            small_robot=self.small_robot,
            other_robots=self.other_robots,
        ))


memory = Memory()
