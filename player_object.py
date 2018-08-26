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
        'True Shot %',
        'EFG%',
        'GmSc',
        'KmGmSc',
        'PPG',
        'ORPG',
        'DRPG',
        'TRPG',
        'APG',
        'SPG',
        'BPG',
        'TOPG',
        'PFpg',
        '+/-pg'
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
        self.offense_rebounds = 0
        self.defense_rebounds = 0
        self.tr = 0  # ?
        self.ast = 0  # Assists?
        self.stl = 0  # Steals
        self.blk = 0  # Blocks
        self.to = 0  # ?
        self.pf = 0  # Personal Foul?
        self.plus_minus = 0  # ?
        self.pts = 0  # ?

    def emit_row(self):
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
            self.offense_rebounds,
            self.defense_rebounds,
            self.tr,
            self.ast,
            self.stl,
            self.blk,
            self.to,
            self.pf,
            self.plus_minus,
            self.pts,
            self.get_true_shot_percent(),
            self.get_effective_fg_percent(),
            self.get_gamescore(),
            self.get_km_gamescore(),
            self.get_ppg(),
            self.get_orpg(),
            self.get_drpg(),
            self.get_trpg(),
            self.get_apg(),
            self.get_spg(),
            self.get_bpg(),
            self.get_topg(),
            self.get_pfpg(),
            self.get_plus_minus_pg()
        ]

    def get_true_shot_percent(self):
        coefficient = 0.475
        shot_factor = self.fg_attempted + (coefficient * self.free_throws_attempted)
        if shot_factor != 0:
            return self.pts / (2 * shot_factor)
        return 0  # Return zero or is None better?

# 100*Points / [2 * (FGA + .44*FTA) ]

    def get_effective_fg_percent(self):
        coefficient = 0.5
        efg = self.fg_made + coefficient * self.three_point_made
        if self.fg_attempted != 0:
            return efg / self.fg_attempted
        return 0

    def get_gamescore(self):
        return self.pts + 0.4 * self.fg_attempted - 0.4 * (self.free_throws_attempted - self.free_throws_made) + 0.7 * self.offense_rebounds + 0.3 * self.defense_rebounds + self.stl + 0.7 * self.ast + 0.7 * self.blk - 0.4 * self.pf - self.to

    def get_km_gamescore(self):
        return self.pts + 0.4 * self.fg_attempted - 0.4 * (self.free_throws_attempted - self.free_throws_made) + 1.0 * self.offense_rebounds + 0.5 * self.defense_rebounds + 1.4 * self.stl + 1.0 * self.ast + 1.4 * self.blk - 0.4 * self.pf - 1.4 * self.to

    def get_ppg(self):
        if self.games != 0 and self.pts != 0:
            return self.pts / self.games
        return 0

    def get_orpg(self):
        if self.games != 0 and self.offense_rebounds != 0:
            return self.offense_rebounds / self.games
        return 0

    def get_drpg(self):
        if self.games != 0 and self.defense_rebounds != 0:
            return self.defense_rebounds / self.games
        return 0

    def get_trpg(self):
        if self.games != 0 and self.tr != 0:
            return self.tr / self.games
        return 0

    def get_apg(self):
        if self.games != 0 and self.ast != 0:
            return self.ast / self.games
        return 0

    def get_spg(self):
        if self.games != 0 and self.stl != 0:
            return self.stl / self.games
        return 0

    def get_bpg(self):
        if self.games != 0 and self.blk != 0:
            return self.blk / self.games
        return 0

    def get_topg(self):
        if self.games != 0 and self.to != 0:
            return self.to / self.games
        return 0

    def get_pfpg(self):
        if self.games != 0 and self.pf != 0:
            return self.pf / self.games
        return 0

    def get_plus_minus_pg(self):
        if self.games != 0 and self.plus_minus != 0:
            return self.plus_minus / self.games
        return 0



















