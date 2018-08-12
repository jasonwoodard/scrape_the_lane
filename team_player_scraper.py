import soup_kitchen
import player_object


class TeamPlayerScraper:
    def __init__(self, team_page):
        self.team_soup = soup_kitchen.get_soup(team_page)
        self.team_name = self.get_team_name()

    def get_team_player_data(self):
        players = []
        rows = self._get_team_rows()
        for row in rows:
            player = self._extract_player_row(row)
            players.append(player)

        return players

    def _get_team_rows(self):
        return self.team_soup.select('tr.even, tr.odd')

    def get_team_name(self):
        # name = self.team_soup.find()
        return 'get team name not implemented'
        pass

    @staticmethod
    def _extract_player_row(row):
        player = player_object.Player(row)
        # Assume row is tr.even or tr.odd from player table with the following cells
        # Name	Yr	Ht	Pos		Gms	Min	FG	FG%	3P	3P%	FT	FT%	OR	DR	TR	Ast	Stl	Blk	TO	PF	+/-	Pts
        cells = row.find_all('td')
        player.name = cells[0].contents[0]
        player.year = cells[1].contents[0]
        player.height = cells[2].contents[0]
        player.position = cells[3].contents[0]
        player.games = cells[4]
        player.min = cells[5].contents[0]
        return player
