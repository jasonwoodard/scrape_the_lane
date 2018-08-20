
class Player(object):

    RowHeader = [
        'Id',
        'Name',
        'Yr',
        'Ht',
        'Pos',
        'Gms',
        'Min',
        'FG',
        'FG_Made',
        'FG_Attempt',
        'FG %',
        '3P',
        '3P %',
        'FT',
        'FT_Made',
        'FT_Attempt',
        'FT %',
        'OR',
        'DR',
        'TR',
        'Ast',
        'Stl',
        'Blk',
        'TO',
        'PF',
        '+ / -',
        'Pts'
    ]

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
        self.fg_made = 0
        self.fg_attempted = 0
        self.fg_pct = 0
        self.three_point = ''
        self.three_point_made = 0
        self.three_point_attempted = 0
        self.three_point_pct = 0
        self.free_throws = 0
        self.free_throws_made = 0
        self.free_throw_attempted = 0
        self.free_throw_pct = 0
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

    def emit_row(self):
        return [
            self.id,
            self.name,
            self.year,
            self.height,
            self.position,
            self.games,
            self.min,
            self.fg,
            self.fg_made,
            self.fg_attempted,
            self.fg_pct,
            self.three_point,
            self.three_point_made,
            self.three_point_attempted,
            self.three_point_pct,
            self.free_throws,
            self.free_throws_made,
            self.free_throw_attempted,
            self.free_throw_pct,
            self.offense_rating,
            self.defense_rating,
            self.tr,
            self.ast,
            self.stl,
            self.blk,
            self.to,
            self.pf,
            self.plus_minus,
            self.pts
        ]

    def get_fg_true_shot(self):
        # use properties on the player, e.g. self.three_point_made to return a value.
        true_shot = -1
        # Your function goes here
        return true_shot
