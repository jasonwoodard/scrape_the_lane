
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
        'FG%',
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
        'STL', # Steals were missed in initial coding
        'BLK',
        'TO', # turnovers missed in initial coding
        'PF',
        '+ / -',
        'PTS',
        'opp_games',
        'opp_minutes',
        'opp_FG',
        'opp_FGM',
        'opp_FGA',
        'opp_FG%',
        'opp_3P',
        'opp_3PM',
        'opp_3PA',
        'opp_3P%',
        'opp_FT',
        'opp_FTM',
        'opp_FTA',
        'opp_FT%',
        'opp_OR',
        'opp_DR',
        'opp_TR',
        'opp_AST',
        'opp_STL', # Steals were missed in initial coding
        'opp_BLK',
        'opp_TO', # turnovers missed in initial coding
        'opp_PF',
        'opp_+ / -',
        'opp_PTS',
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
        self.ft_made = 0
        self.ft_attempted = 0
        self.ft_pct = 0
        self.oreb = 0
        self.dr = 0
        self.tr = 0
        self.ast = 0
        self.stl = 0
        self.blk = 0
        self.to = 0
        self.pf = 0
        self.plus_minus = 0
        self.pts = 0
        self.opp_gms = -1
        self.opp_minutes = 0
        self.opp_minutes_float = 0
        self.opp_fg = ''
        self.opp_fg_made = 0
        self.opp_fg_attempted = 0
        self.opp_fg_pct = 0
        self.opp_three_point = ''
        self.opp_three_point_made = 0
        self.opp_three_point_attempted = 0
        self.opp_three_point_pct = 0
        self.opp_ft = ''
        self.opp_ft_made = 0
        self.opp_ft_attempted = 0
        self.opp_ft_pct = 0
        self.opp_oreb = 0
        self.opp_dr = 0
        self.opp_tr = 0
        self.opp_ast = 0
        self.opp_stl = 0
        self.opp_blk = 0
        self.opp_to = 0
        self.opp_pf = 0
        self.opp_plus_minus = 0
        self.opp_pts = 0
    def emit_row(self):
        row = [
            self.name,
            self.id,
            self.conference_id,
            self.gms,
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
            self.ft_made,
            self.ft_attempted,
            self.ft_pct,
            self.oreb,
            self.dr,
            self.tr,
            self.ast,
            self.stl,
            self.blk,
            self.to,
            self.pf,
            self.plus_minus,
            self.pts,
            self.opp_gms,
            self.opp_minutes_float,
            self.opp_fg,
            self.opp_fg_made,
            self.opp_fg_attempted,
            self.opp_fg_pct,
            self.opp_three_point,
            self.opp_three_point_made,
            self.opp_three_point_attempted,
            self.opp_three_point_pct,
            self.opp_ft,
            self.opp_ft_made,
            self.opp_ft_attempted,
            self.opp_ft_pct,
            self.opp_oreb,
            self.opp_dr,
            self.opp_tr,
            self.opp_ast,
            self.opp_stl,
            self.opp_blk,
            self.opp_to,
            self.opp_pf,
            self.opp_plus_minus,
            self.opp_pts
        ]
        # Catch if the header and the row length don't match.
        assert len(Team.RowHeader) == len(row)
        return row
