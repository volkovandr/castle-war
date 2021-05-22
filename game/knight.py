import random

class Knight:
    position = 0
    road = None
    team = 0
    gs = None

    def __init__(self, _road, _team, _gs):
        self.road = _road
        self.team = _team
        self.gs = _gs

    def tick(self):
        self.position += 1
        if self.position >= self.road.length:
            self.process_road_end()

    def process_road_end(self):
        if self.road.castle.team == self.team:
            self.road.castle.knights += 1
        elif random.random() >= 0.5:
            self.road.castle.knights -= 1
            if self.road.castle.knights < 0:
                self.road.castle.team = self.team
        gs.kill_knight(self)

