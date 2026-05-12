# =========================
# Q8 Class Variable
# =========================

class Player:
    player_count = 0

    def __init__(self, name, level):
        self.name = name
        self.level = level
        Player.player_count += 1


p1 = Player("Rohit", 5)
p2 = Player("Virat", 8)

print("Total Players:", Player.player_count)
