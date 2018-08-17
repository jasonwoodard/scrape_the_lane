import re

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

    def _extract_player_row(self, row):
        player = player_object.Player(row)
        # Assume row is tr.even or tr.odd from player table with the following cells
        # Name	Yr	Ht	Pos	[spacer] Gms Min FG	FG%	3P	3P%	FT	FT%	OR	DR	TR	Ast	Stl	Blk	TO	PF	+/-	Pts
        cells = row.find_all('td')

        # Extract data from cells (TDs) and populate the player object.
        player.id = self._get_player_id(cells[0])
        player.name = self._get_player_name(cells[0])
        player.year = self._get_content(cells, 1)
        player.height = self._get_content(cells, 2)
        player.position = self._get_content(cells, 3)
        # Column 4 is a spacer column.
        player.games = self._get_content(cells, 5)
        player.min = self._get_content(cells, 6)
        player.fg = self._get_content(cells, 7)
        player.fg_pct = self._get_content(cells, 8)
        player.three_p = self._get_content(cells, 9)
        player.three_p_pct = self._get_content(cells, 10)
        player.ft = self._get_content(cells, 11)
        player.ft_pct = self._get_content(cells, 12)
        player.offense_rating = self._get_content(cells, 13)
        player.defense_rating = self._get_content(cells, 14)
        player.tr = self._get_content(cells, 15)
        player.ast = self._get_content(cells, 16)
        player.stl = self._get_content(cells, 17)
        player.blk = self._get_content(cells, 18)
        player.to = self._get_content(cells, 19)
        player.pf = self._get_content(cells, 20)
        player.plus_minus = self._get_content(cells, 21)
        player.pts = self._get_content(cells, 22)

        return player

    def _get_content(self, cells, index):
        cell = cells[index]
        value = cell.contents[0]
        return value

    def _get_player_name(self, name_td):
        # <a href="player?pid=p9DE5067489" class="player">Joseph Piccione</a>
        return name_td.find('a').text

    def _get_player_id(self, name_td):
        # <a href="player?pid=p9DE5067489" class="player">Joseph Piccione</a>
        href = name_td.find('a')['href']
        # href should be 'player?pid=p9DE5067489'
        # use regular expression to match part after equals sign.
        matches = re.search(r'pid=(p\w+)', href)
        # if a match is found return value otherwise return -1
        return matches.group(1) if matches else -1
