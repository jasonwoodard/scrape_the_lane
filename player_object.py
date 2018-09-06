class Player(object):
    RowHeader = [
        'Player Name',
        'Team Name',
        'Conf',
        'Yr',
        'Ht',
        'Pos',
        'Gms',
        'Min',
        'PPG',
        'ORPG',
        'DRPG',
        'TRPG',
        'APG',
        'SPG',
        'BPG',
        'TOPG',
        'PFpg',
        '+/-pg',
        'FG%',
        '2P%',
        '3P%',
        'FT%',
        'True Shot %',
        'EFG%',
        'GmSc',
        'KmGmSc',
        'FGM',
        'FGA',
        '2PM',
        '2PA',
        '3PM',
        '3PA',
        'FTM',
        'FTA',
        'PP30',
        'OR30',
        'DR30',
        'TR30',
        'Ast30',
        'Stl30',
        'Blk30',
        'To30',
        'PF30',
        '+/- 30',
        'Pts',
        'OR',
        'DR',
        'TR',
        'Ast',
        'Stl',
        'Blk',
        'TO',
        'PF',
        '+ / -',
        'PId',
        'Team #',
       # 'FG',
       # '3P',
       # 'FT',
    ]

    def __init__(self):
        self.id = -1  # The unique player identification number
        self.team = None
        self.name = ''  # Player's name
        self.year = ''  # The class the player is in college (Fr = Freshman, So = Sophomore, Jr = Junior, Se = Senior)
        self.height = ''  # The height of the player in feet'inches
        self.height_inches = 0  # The height of the player in inches
        self.position = '' # Position the player is currently playings (PG, SG, SF, PF, C, bPG, bSG, bSF, bPF, bC, NA)
        self.games = 0  # Number of games played
        self.minutes = ''  # Number of minutes played as time value
        self.minutes_float = 0  # Minutes value as a decimal
        self.fg = ''  # Number of field goals made-attempted
        self.fg_made = 0  # Number of field goals made
        self.fg_attempted = 0  # Number of Field goal shots attempted
        self.fg_pct = 0  # Percentage of field goal attempts made
        self.three_point = ''  # three pointers made-attempted
        self.three_point_made = 0  # of three pointers made
        self.three_point_attempted = 0  # number of three pointers attempted
        self.three_point_pct = 0  # Percentage of three-point shots made
        self.free_throws = 0  # Free throws made - attempted
        self.free_throws_made = 0  # Free throws made
        self.free_throws_attempted = 0  # Free Throw attempts
        self.free_throw_pct = 0  # Percentage of free throws made
        self.offense_rebounds = 0  # Offensive rebounds
        self.defense_rebounds = 0  # Defensive rebounds
        self.tr = 0  # Total Rebounds
        self.ast = 0  # Assists
        self.stl = 0  # Steals
        self.blk = 0  # Blocks
        self.to = 0  # Turnovers 
        self.pf = 0  # Personal Foul
        self.plus_minus = 0  # Plus minus = Team Points - Opponent Points while player is on the court
        self.pts = 0  # Points

    def emit_row(self):
        return [
            self.name,
            self.team.name,
            self.team.conference_id,
            self.year,
            self.height_inches,
            self.position,
            self.games,
            self.minutes,
            self.get_ppg(),
            self.get_orpg(),
            self.get_drpg(),
            self.get_trpg(),
            self.get_apg(),
            self.get_spg(),
            self.get_bpg(),
            self.get_topg(),
            self.get_pfpg(),
            self.get_plus_minus_pg(),
            self.fg_pct,
            self.get_two_point_pct(),
            self.three_point_pct,
            self.free_throw_pct,
            self.get_true_shot_percent(),
            self.get_effective_fg_percent(),
            self.get_gamescore(),
            self.get_km_gamescore(),
            self.fg_made,
            self.fg_attempted,
            self.get_two_point_made(),
            self.get_two_point_attempted(),
            self.three_point_made,
            self.three_point_attempted,
            self.free_throws_made,
            self.free_throws_attempted,
            self.get_pts_thirty(),
            self.get_oreb_thirty(),
            self.get_dreb_thirty(),
            self.get_treb_thirty(),
            self.get_ast_thirty(),
            self.get_stl_thirty(),
            self.get_blk_thirty(),
            self.get_to_thirty(),
            self.get_fouls_thirty(),
            self.get_plus_minus_thirty(),
            self.pts,
            self.offense_rebounds,
            self.defense_rebounds,
            self.tr,
            self.ast,
            self.stl,
            self.blk,
            self.to,
            self.pf,
            self.plus_minus,
            self.id,
            self.team.id,
            #self.fg,
            #self.three_point,
            #self.free_throws,
        ]

    def get_true_shot_percent(self):
        coefficient = 0.475
        shot_factor = self.fg_attempted + (coefficient * self.free_throws_attempted)
        if shot_factor != 0:
            return self.pts / (2 * shot_factor)
        return 0  # Return zero or is None better?

    # 100*Points / [2 * (FGA + .44*FTA) ]

    def get_gamescore(self):
        return self._calc_game_score(
            or_coefficient=0.7,
            dr_coefficient=0.3,
            stl_coefficient=1.0,
            ast_coefficient=0.7,
            blk_coefficient=0.7,
            pf_coefficient=0.4,
            to_coefficient=1.0)

    def get_km_gamescore(self):
        return self._calc_game_score(
            or_coefficient=1.0,
            dr_coefficient=0.5,
            stl_coefficient=1.4,
            ast_coefficient=1.0,
            blk_coefficient=1.4,
            pf_coefficient=0.4,
            to_coefficient=1.4)

    def _calc_game_score(self,
                         or_coefficient,
                         dr_coefficient,
                         stl_coefficient,
                         ast_coefficient,
                         blk_coefficient,
                         pf_coefficient,
                         to_coefficient):
        # fg and free throw are constant between gamescore and km_gamescore
        fg_attempted_factor = (0.4 * self.fg_attempted)
        free_throws_factor = 0.4 * (self.free_throws_attempted - self.free_throws_made)

        # use the coefficients for each method to calculator the factor
        or_factor = (or_coefficient * self.offense_rebounds)
        dr_factor = (dr_coefficient * self.defense_rebounds)
        stl_factor = (stl_coefficient * self.stl)
        ast_factor = (ast_coefficient * self.ast)
        blk_factor = (blk_coefficient * self.blk)
        pf_factor = (pf_coefficient * self.pf)
        to_factor = (to_coefficient * self.to)
        return self.pts + fg_attempted_factor - free_throws_factor + or_factor + dr_factor + stl_factor + ast_factor + blk_factor - pf_factor - to_factor

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
    
    def get_effective_fg_percent(self):
        coefficient = 0.5
        three_point_factor = coefficient * self.three_point_made
        efg = self.fg_made + three_point_factor
        if self.fg_attempted != 0:
            return efg / self.fg_attempted
        return 0
   
    def get_two_point_made(self):
        # Every shot taken is either a two point or three point field goal attempt.  
        # Field goal attempts include both two point attempts and three point attempts.
        # Three point attempts are a sub-category of field goal attempts.
        # Since these are the only two types of shots, the formula is simple.
        # Since this is subtraction, we do not need to check for zero (because that'd be fine)
        return self.fg_made - self.three_point_made
    
    def get_two_point_attempted(self):
        return self.fg_attempted - self.three_point_attempted
    
    def get_two_point_pct(self):
        two_point_made = self.get_two_point_made()
        two_point_attempted = self.get_two_point_attempted()

        if two_point_attempted != 0:
            return two_point_made / two_point_attempted
        return 0
    
    # PER 30 MINUTE STATS:
    # PTS, Offensive REB, Defensive REB, Total REB, Assists, Steals, Blocks, Personal Fouls, plus/minus

    def get_pts_thirty(self):
        return self._calc_per_thirty(self.pts)
    
    def get_oreb_thirty(self):
        return self._calc_per_thirty(self.offense_rebounds)
    
    def get_dreb_thirty(self):
        return self._calc_per_thirty(self.defense_rebounds)
    
    def get_treb_thirty(self):
        return self._calc_per_thirty(self.tr)
    
    def get_ast_thirty(self):
        return self._calc_per_thirty(self.ast)
    
    def get_stl_thirty(self):
        return self._calc_per_thirty(self.stl)
    
    def get_blk_thirty(self):
        return self._calc_per_thirty(self.blk)
    
    def get_to_thirty(self):
        return self._calc_per_thirty(self.to)

    def get_fouls_thirty(self):
        return self._calc_per_thirty(self.pf)

    def get_plus_minus_thirty(self):
        return self._calc_per_thirty(self.plus_minus)

    def _calc_per_thirty(self, numerator):
        minutes = self.minutes_float
        if minutes != 0:
            return (numerator / minutes) * 30
        return 0
