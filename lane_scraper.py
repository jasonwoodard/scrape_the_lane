class LaneScraper:
    def __init__(self):
        pass

    def get_team_player_data(self, team_page):
        players = []

        rows = self.get_team_rows(team_page)

        for row in rows:

            player = self.extract_player_row(row)
            players.append(player)

        return players

    def get_team_rows(self, team_page):


    def extract_player_row(self, row):
        pass
