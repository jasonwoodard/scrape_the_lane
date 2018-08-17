
class Player(object):

    PlayerRowHeader = '''
        Id, Name, Yr, Ht, Pos, Gms, Min, FG, FG%, 3P, 3P%, FT, FT%, OR, DR, TR, Ast, Stl, Blk, TO, PF, +/-, Pts
        '''

    PlayerRowTemplate = '''
        {{id}}, {{name}}, {{year}}, {{height}}, {{position}}, {{games}}, {{min}}, {{fg}}, {{fg_pct}}, {{three_p}}, {{three_p_pct}}, {{ft}}, {{ft_pct}}, {{offense_rating}}, {{defense_rating}}, {{tr}}, {{ast}}, {{stl}}, {{blk}}, {{to}}, {{pf}}, {{plus_minus}}, {{pts}}
        '''

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
        self.ft = 0
        self.ft_pct = 0
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

