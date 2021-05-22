from knight import Knight

class Castle:
    team = 0
    knights = 0
    level = 1
    orders = []
    gs = None

    def __init__(self, _team, _gs):
        self.team = _team
        self.gs = _gs

    def tick(self):
        self.increment_knights(self)
        self.process_send_knights_orders(self)

    def increment_knights(self):
        if self.knights > self.level * 10:
            self.knights -= 1
        elif self.knights < self.level * 10:
            self.knights += 1

    def is_upgradable(self):
        return self.knights >= self.level * 5
    
    def upgrade(self):
        self.knights = self.knights - self.level * 5
        self.level += 1

    def order_send_knights(self, road):
        knights_to_send = self.knights
        for order in self.orders:
            knights_to_send -= order.knights_to_send
        knights_to_send = int ((knights_to_send + 1) / 2)
        
        if knights_to_send > 0:
            self.orders.append(Order(road, knights_to_send))


    def process_send_knights_orders(self):
        if self.orders.__len__() > 0:
            order = self.orders[0]
            self.gs.add_knight(Knight(order.road, self.team, self.gs))
            order.knights_to_send -= 1
            if order.knights_to_send == 0:
                self.orders.remove(order)


class Order:
    road = None
    knights_to_send = 0

    def __init__(self, _road, _knights_to_send):
        self.road = _road
        self.knights_to_send = _knights_to_send