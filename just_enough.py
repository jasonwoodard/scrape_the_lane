from player_object import Player

row = None
p = Player(row)

# Setup
p.fg_attempted = 17
p.free_throws_attempted = 12
p.pts = 16

# Function output
print p.get_true_shot_percent()