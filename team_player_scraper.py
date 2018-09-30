import re

import soup_kitchen as kitchen
import player_object

from team_scraper import TeamScraper


class TeamPlayerScraper:
    def __init__(self, team_page, team_id):
        self.team_page_soup = kitchen.get_soup(team_page)
        self.team_id = team_id

    def get_team_player_data(self):
        players = []

        team_scraper = TeamScraper(self.team_id, self.team_page_soup,)
        team = team_scraper.get_team()

        rows = self._get_player_rows()
        for row in rows:
            player = self._extract_player_row(row)
            player.team = team
            players.append(player)

        return players

    def _get_player_rows(self):
        return self.team_page_soup.select('tr.even, tr.odd')

    # def _get_team(self, team_id):
    #     header = soup_kitchen.get_team_header(self.team_page_soup)
    #     name = self._get_team_name(header)
    #     conf_id = self._get_team_conference(header)
    #
    #     team = team_object.Team()
    #     team.team_id = team_id
    #     team.name = name
    #     team.conference_id = conf_id
    #     return team

    def _extract_player_row(self, row):
        # Attach row to player object incase we need it later.
        player = player_object.Player()

        cells = row.find_all('td')

        # Extract data from cells (TDs) by cell ID and populate the player object.
        # RISK: If the order of the cells changes, we need to revise this section.
        player.id = self._get_player_id(cells[0])
        player.name = self._get_player_name(cells[0])
        player.year = kitchen.get_content(cells, 1)

        # Height
        height_raw = kitchen.get_content(cells, 2)
        player.height = height_raw
        height_split = height_raw.split('-')
        feet_inches = int(height_split[0]) * 12
        player.height_inches = feet_inches + int(height_split[1])
        
        player.weight = kitchen.get_content(cells, 3) # Added weight
        player.position = kitchen.get_content(cells, 4) # renumbered to 4

        # Column 5 is a spacer column. Skip it.

        player.games = kitchen.get_float_content(cells, 6)
        player.minutes = kitchen.get_content(cells, 7)
        player.minutes_float = self.get_minutes_float(player.minutes)

        # Field Goals
        # Get the 'raw' value shown on screen and put it on the player object.
        fg_raw = kitchen.get_content(cells, 8)
        player.fg = fg_raw

        # Field Goals split out
        # Split raw value into made - attempted. Assign those values to the player object.
        fg_split = fg_raw.split('-')
        player.fg_made = float(fg_split[0])
        player.fg_attempted = float(fg_split[1])
        player.fg_pct = kitchen.get_content(cells, 9)

        # Three Pointers
        three_p_raw = kitchen.get_content(cells, 10)
        player.three_point = three_p_raw

        # Three Pointer split out
        three_p_split = three_p_raw.split('-')
        player.three_point_made = float(three_p_split[0])
        player.three_point_attempted = float(three_p_split[1])
        player.three_point_pct = kitchen.get_content(cells, 11)

        # Free Throws
        ft_raw = kitchen.get_content(cells, 12)
        player.free_throws = ft_raw

        # Free Throws split out
        # ft_split = fg_raw.split('-')
        ft_split = ft_raw.split('-')
        player.free_throws_made = float(ft_split[0])
        player.free_throws_attempted = float(ft_split[1])
        player.free_throw_pct = kitchen.get_content(cells, 13)

        player.offense_rebounds = kitchen.get_float_content(cells, 14)
        player.defense_rebounds = kitchen.get_float_content(cells, 15)
        player.tr = kitchen.get_float_content(cells, 16)
        player.ast = kitchen.get_float_content(cells, 17)
        player.stl = kitchen.get_float_content(cells, 18)
        player.blk = kitchen.get_float_content(cells, 19)
        player.to = kitchen.get_float_content(cells, 20)
        player.pf = kitchen.get_float_content(cells, 21)
        player.plus_minus = kitchen.get_float_content(cells, 22)
        player.pts = kitchen.get_float_content(cells, 23)

        return player

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

    @staticmethod
    def get_minutes_float(minutes):
        # expect minutes in string form like '00:00'
        parts = minutes.split(':')
        min_part = int(parts[0])
        sec_part = int(parts[1])
        return min_part + (sec_part/60)
