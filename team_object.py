
class Team(object):

    RowHeader = [
        'name',
        'id',
        'conference',
        'games',
        'minutes',
        'FG',
        'FGM',
        'FGA',
        '3P',
        '3PM',
        '3PA',
        '3P%',
        'FT',
        'FTM',
        'FTA',
        'FT%',
        'OR',
        'DR',
        'TR',
        'AST',
        'BLK',
        'PF',
        '+ / -',
        'PTS'
    ]

    def __init__(self):
        self.name = ''
        self.id = -1
        self.conference_id = -1
        self.gms = -1
        self.minutes = 0
        self.minutes_float = 0
        self.fg = ''
        self.fg_made = 0
        self.fg_attempted = 0
        self.fg_pct = 0
        self.three_point = ''
        self.three_point_made = 0
        self.three_point_attempted = 0
        self.three_point_pct = 0
        self.ft = ''
        self.ft_attempted = 0
        self.ft_made = 0
        self.ft_pct = 0
        self.oreb = 0
        self.dr = 0
        self.tr = 0
        self.ast = 0
        self.blk = 0
        self.pf = 0
        self.plus_minus = 0
        self.pts = 0

    def emit_row(self):
        return [
            self.name,
            self.id,
            self.conference_id,
            self.gms,
            self.minutes,
            self.minutes_float,
            self.fg,
            self.fg_made,
            self.fg_attempted,
            self.fg_pct,
            self.three_point,
            self.three_point_made,
            self.three_point_attempted,
            self.three_point_pct,
            self.ft,
            self.ft_attempted,
            self.ft_made,
            self.ft_pct,
            self.oreb,
            self.dr,
            self.tr,
            self.ast,
            self.blk,
            self.pf,
            self.plus_minus,
            self.pts
        ]
