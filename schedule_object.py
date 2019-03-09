'''
This is the schedule object class.  We know that it will always need to have:

1. The team id (from the team_id_counter).
2. The game #/ID (E1, E2, E3, 1 to 24).
3. The date and time the game was played.
4. The Power Ranking of the opponent. (Strip away the # sign before the integer)
5. The name of opponent
6. The record of the opponent (split into wins and losses at '-')
7. The coach name of opponent
8. The result of the game (split this into team score and opponent score at '-')
    a. W for win or L for loss
    b. Team Score
    c. Opponent's Score
9. The team's win loss record and conference
    a. This gets tricky because the overall record is split at the '-'
    b. While the conference record is inside the (15-0) and split at the '-'
10. The Tempo the team played
11. The Style of defense the team played
12. The 3-point shooting setting the team played.
'''

class Schedule(object):
    RowHeader = [
        'id', # this is the team id from the team_id_counter
        'game_number',
        'date',
        'opp_PR',
        'opp_name',
        'opp_wins',
        'opp_losses',
        'opp_coach',
        'w_or_l',
        'score',
        'opp_score',
        'wins',
        'losses',
        'conf_wins',
        'conf_losses',
        'tempo',
        'defense',
        'three_point_shooting',
    ]


    def __init__(self):
        self.id = -1
        self.game_number = -1
        self.date = -1
        self.opp_PR = 0
        self.opp_name = 0
        self.opp_wins = 0
        self.opp_losses = 0
        self.opp_coach = 0
        self.w_or_l = ''
        self.score = 0
        self.opp_score = 0
        self.wins = 0
        self.losses = 0
        self.conf_wins = 0
        self.conf_losses = 0
        self.tempo = ''
        self.defense = ''
        self.three_point_shooting = ''
    def emit_row(self):
        row = [
            self.id,
            self.game_number,
            self.date,
            self.opp_PR,
            self.opp_name,
            self.opp_wins,
            self.opp_losses,
            self.opp_coach,
            self.w_or_l,
            self.score,
            self.opp_score,
            self.wins,
            self.losses,
            self.conf_wins,
            self.conf_losses,
            self.tempo,
            self.defense,
            self.three_point_shooting,
        ]
        # Catch if the header and the row length don't match.
        assert len(Schedule.RowHeader) == len(row)
        return row
