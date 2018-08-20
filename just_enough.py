from player_object import Player

row = None
p = Player(row)

# Setup
p.fg_attempted = 17
p.fg_made = 12

# Function output
print p.get_fg_true_shot()