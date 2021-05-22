class Game_situation:
    knights = []
    castles = []
    roads = []

    def kill_knight(self, knight):
        self.knights.remove(knight)

    def add_knight(self, knight):
        self.knights.append(knight)

    def is_game_finished(self):
        team = self.castles[0].team
        for castle in self.castles:
            if castle.team != team:
                return False
        return True