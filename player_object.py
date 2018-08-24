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
        '2P_Made'
        '2P_Attempt'
        '2P_%'
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
        self.offensive_rebounds = 0 # Offensive rebounds --> Changed name of attribute
        self.defensive_rebounds = 0 # Defensive rebounds --> Changed name of attribute
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
            self.get_two_point_made()
            self.get_two_point_attempted()
            self.get_two_point_pct()
        ]

    def get_true_shot_percent(self):
        coefficient = 0.475
        shot_factor = self.fg_attempted + (coefficient * self.free_throws_attempted)
        if shot_factor != 0:
            return self.pts / (2 * shot_factor)
        return 0  # Return zero or is None better? --> I prefer zero as it will have the entire row be the same type of data.
    
    def get_two_point_made(self):
        # Every shot taken is either a two point or three point field goal attempt.  
        # Field goal attempts include both two point attempts and three point attempts.
        # Three point attempts are a sub-category of field goal attempts.
        # Since these are the only two types of shots, the formula is simple.
        # Since this is subtraction, we do not need to check for zero (because that'd be fine)
        return self.fg_made - self.three_point_made
    
    def get_two_point_attempted(self):
        return self.fg_attempted - self.free_throws_attempted
    
    def get_two_point_pct():
        # Here, I'm not sure how to reference the values returned by the previous functions.
        # I need to divide the result of  get_two_point_made by get_two_point_attempted
        # I also need to check for zero
        two_pct = self.get_two_point_made()/self.get_two_point_attempted()
        if two_pct != 0:
            return two_pct
        return 0
       
        

        
