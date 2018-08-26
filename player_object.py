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
        '+/-pg',
        '2P_Made',
        '2P_Attempt',
        '2P_%',
        'PP30',
        'OR30',
        'DR30',
        'TR30',
        'Ast30',
        'Stl30',
        'Blk30',
        'To30',
        'PF30',
        '+ / - 30',
    ]

    def __init__(self, player_row):
        self.row = player_row
        self.team = None 
        self.id = -1 # The unique player identification number
        self.name = '' # Player's name
        self.year = '' # The class the player is in college (Fr = Freshman, So = Sophomore, Jr = Junior, Se = Senior)
        self.height = '' # The height of the player in feet'inches
        self.position = '' # The position the player is currently playings (PG, SG, SF, PF, C, bPG, bSG, bSF, bPF, bC, NA)
        self.games = '' # Number of games played
        self.minutes = '' # Number of minutes played
        self.minutes_float = 0 # Minutes value as a decimal
        self.fg = '' # Number of field goals made-attempted
        self.fg_made = 0 # Number of field goals made
        self.fg_attempted = 0 # Number of Field goal shots attempted
        self.fg_pct = 0 # Percentage of field goal attempts made 
        self.three_point = '' # three pointers made-attempted
        self.three_point_made = 0 # of three pointers made
        self.three_point_attempted = 0 # number of three pointers attempted
        self.three_point_pct = 0 # Percentage of three-point shots made
        self.free_throws = 0 # Free throws made - attempted 
        self.free_throws_made = 0 # Free throws made
        self.free_throws_attempted = 0 # Free Throw attempts
        self.free_throw_pct = 0 # Percentage of free throws made
        self.offense_rebounds = 0 # Offensive rebounds --> Changed name of attribute
        self.defense_rebounds = 0 # Defensive rebounds --> Changed name of attribute
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
            self.get_plus_minus_pg(),
            self.get_two_point_made(),
            self.get_two_point_attempted(),
            self.get_two_point_pct(),
            self.get_pts_thirty(),
            self.get_oreb_thirty(),
            self.get_dreb_thirty(),
            self.get_treb_thirty(), # Not sure this is the right function was get_tr_thirty()
            self.get_ast_thirty(),
            self.get_stl_thirty(),
            self.get_blk_thirty(),
            self.get_to_thirty(),
            self.get_fouls_thirty(),
            self.get_plus_minus_thirty()
        ]

    def get_true_shot_percent(self):
        coefficient = 0.475
        shot_factor = self.fg_attempted + (coefficient * self.free_throws_attempted)
        if shot_factor != 0:
            return self.pts / (2 * shot_factor)
        return 0  # Return zero or is None better?

# 100*Points / [2 * (FGA + .44*FTA) ]

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
        # Here, I'm not sure how to reference the values returned by the previous functions.
        # [JW] Use local variables to make your life easier.
        # I need to divide the result of  get_two_point_made by get_two_point_attempted
        # I also need to check for zero
        # [JW] Sure. local variables help with this and make your zero check easier.

        two_point_made = self.get_two_point_made()
        two_point_attempted = self.get_two_point_attempted()

        if two_point_attempted != 0:
            return two_point_made / two_point_attempted
        return 0
    
    ### PER 30 MINUTE STATS (PTS, Offensive REB, Defensive REB, Total REB, Assists, Steals, Blocks, Personal Fouls, plus/minus)
    ### Do I need a seperate function for each of these or could I return a list that then returns values that are assigned to spots on the emit function
    
    def get_pts_thirty(self):
        if self.minutes_float !=0:
            return (self.pts / self.minutes_float) * 30
        return 0
    
    def get_oreb_thirty(self):
        if self.minutes_float != 0:
            return (self.offense_rebounds / self.minutes_float) * 30
        return 0
    
    def get_dreb_thirty(self):
        if self.minutes_float != 0:
            return (self.defense_rebounds / self.minutes_float) * 30
        return 0
    
    def get_treb_thirty(self):
        if self.minutes_float != 0:
            return (self.tr / self.minutes_float) * 30
        return 0
    
    def get_ast_thirty(self):
        if self.minutes_float != 0:
            return (self.ast / self.minutes_float) * 30
        return 0   
    
    def get_stl_thirty(self):
        if self.minutes_float != 0:
            return (self.stl / self.minutes_float) * 30
        return 0  
    
    def get_blk_thirty(self):
        if self.minutes_float != 0:
            return (self.blk / self.minutes_float) * 30
        return 0
    
    def get_to_thirty(self):
        if self.minutes_float != 0:
            return (self.to / self.minutes_float) * 30
        return 0
    
    def get_fouls_thirty(self):
        if self.minutes_float != 0:
            return (self.pf / self.minutes_float) * 30
        return 0  
    
    def get_plus_minus_thirty(self):
        if self.minutes_float != 0:
            return (self.plus_minus / self.minutes_float) * 30
        return 0      
    
    #### Need to create the function
    #### Need to add the function to the return list
    #### Need to add to the row header
  
