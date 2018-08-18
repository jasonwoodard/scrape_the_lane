
class Player(object):

    PlayerRowHeader = '''
    Id, Name, Yr, Ht, Pos, Gms, Min, FG, FG_Made, FG_Attempt, FG%, 3P, 3P%, FT, FT_Made, FT_Attempt FT%, OR, DR, TR, Ast, Stl, Blk, TO, PF, +/-, Pts'''

    PlayerRowTemplate = '''
    {{id}}, {{name}}, {{year}}, {{height}}, {{position}}, {{games}}, {{min}}, {{fg}}, {{fg_made}}, {{fg_attempted}}, {{fg_pct}}, {{three_point}}, {{three_point_made}}, {{three_point_pct}}, {{free_throws}}, {{free_throws_made}}, {{free_throws_attempted}}, {{free_throws_pct}}, {{offense_rating}}, {{defense_rating}}, {{tr}}, {{ast}}, {{stl}}, {{blk}}, {{to}}, {{pf}}, {{plus_minus}}, {{pts}}
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
