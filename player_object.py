
class Player:
    def __init__(self, player_row):
        self.row = player_row
        self.id = -1
        self.name = ''
        self.year = ''
        self.height = ''
        self.position = ''
        self.games = ''
        self.min = ''
        self.fg = ''
        self.fg_pct = 0
        self.three_p = ''
        self.three_p_pct = 0
        self.offense_rating = 0
        self.defense_rating = 0
        self.tr = 0             # ?
        self.ast = 0            # Assists?
        self.stl = 0            # Steals
        self.blk = 0            # Blocks
        self.to = 0             # ?
        self.pf = 0             # Personal Foul?
        self.plus_minus = 0     # ?
        self.pts = 0            # ?
