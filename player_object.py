class Player(object):
    RowHeader = [
        'Team Id',
        'Team Name',
        'Player Id',
        'Player Name',
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
        '3P_Made',
        '3P_Attempt',
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
        'Pts',
        'True Shot %'
    ]

    def __init__(self, player_row):
        self.row = player_row
        self.team = None
        self.id = -1
        self.name = ''
        self.year = ''
        self.height = ''
        self.position = ''
        self.games = ''
        self.minutes = ''
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
        self.free_throws_attempted = 0
        self.free_throw_pct = 0
        self.offense_rating = 0
        self.defense_rating = 0
        self.tr = 0  # ?
        self.ast = 0  # Assists?
        self.stl = 0  # Steals
        self.blk = 0  # Blocks
        self.to = 0  # ?
        self.pf = 0  # Personal Foul?
        self.plus_minus = 0  # ?
        self.pts = 0  # ?

    def emit_row(self):
        print 'team: {0} player: {1} true_shot: {2}'.format(self.team.id, self.id, self.get_true_shot_percent())
        return [
            self.team.id,
            self.team.name,
            self.id,
            self.name,
            self.year,
            self.height,
            self.position,
            self.games,
            self.minutes,
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
            self.free_throws_attempted,
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
            self.pts,
            self.get_true_shot_percent()
        ]

    def get_true_shot_percent(self):
        coefficient = 0.475
        print 'player: {0} - {1}'.format(self.id, self.name)
        print 'free_throws_attempted value: {0} type:{1}'.format(self.free_throws_attempted,
                                                                 type(self.free_throws_attempted))
        print 'fg_attempted value: {0} type:{1}'.format(self.fg_attempted, type(self.fg_attempted))
        print 'pts value: {0} type:{1}'.format(self.pts, type(self.pts))

        shot_factor = self.fg_attempted + (coefficient * self.free_throws_attempted)
        if shot_factor > 0:
            return self.pts / (2 * shot_factor)
        return 0
