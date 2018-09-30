import re

import soup_kitchen
import player_object
import team_object


class TeamPlayerScraper:
    def __init__(self, team_page, team_id):
        self.team_page_soup = soup_kitchen.get_soup(team_page)
        self.id = team_id
        self.team = self._get_team(team_id)

    def get_team_player_data(self):
        players = []

        rows = self._get_player_rows()
        for row in rows:
            player = self._extract_player_row(row)
            player.team = self.team
            players.append(player)

        return players

    def _get_player_rows(self):
        return self.team_page_soup.select('tr.even, tr.odd')

    def _get_team(self, id):
        header = soup_kitchen.get_team_header(self.team_page_soup)
        name = self._get_team_name(header)
        conf_id = self._get_team_conference(header)

        team = team_object.Team()
        team.id = id
        team.name = name
        team.conference_id = conf_id
        return team

    @staticmethod
    def _get_team_name(element):
        name_element = element.find('span', {'class': 'h1'})
        return name_element.text

    def _get_team_conference(self, element):
        conf_element = element.find('a', {'class': 'conf'})
        return conf_element.text.lstrip('Conf ')

    def _extract_player_row(self, row):
        # Attach row to player object incase we need it later.
        player = player_object.Player()

        cells = row.find_all('td')

        # Extract data from cells (TDs) by cell ID and populate the player object.
        # RISK: If the order of the cells changes, we need to revise this section.
        player.id = self._get_player_id(cells[0])
        player.name = self._get_player_name(cells[0])
        player.year = self._get_content(cells, 1)

        # Height
        height_raw = self._get_content(cells, 2)
        player.height = height_raw
        height_split = height_raw.split('-')
        feet_inches = int(height_split[0]) * 12
        player.height_inches = feet_inches + int(height_split[1])
        
        player.weight = self._get_content(cells, 3) # Added weight
        player.position = self._get_content(cells, 4) # renumbered to 4

        # Column 5 is a spacer column. Skip it.

        player.games = self._get_float_content(cells, 6)
        player.minutes = self._get_content(cells, 7)
        player.minutes_float = self.get_minutes_float(player.minutes)

        # Field Goals
        # Get the 'raw' value shown on screen and put it on the player object.
        fg_raw = self._get_content(cells, 8)
        player.fg = fg_raw

        # Field Goals split out
        # Split raw value into made - attempted. Assign those values to the player object.
        fg_split = fg_raw.split('-')
        player.fg_made = float(fg_split[0])
        player.fg_attempted = float(fg_split[1])
        player.fg_pct = self._get_content(cells, 9)

        # Three Pointers
        three_p_raw = self._get_content(cells, 10)
        player.three_point = three_p_raw

        # Three Pointer split out
        three_p_split = three_p_raw.split('-')
        player.three_point_made = float(three_p_split[0])
        player.three_point_attempted = float(three_p_split[1])
        player.three_point_pct = self._get_content(cells, 11)

        # Free Throws
        ft_raw = self._get_content(cells, 12)
        player.free_throws = ft_raw

        # Free Throws split out
        # ft_split = fg_raw.split('-')
        ft_split = ft_raw.split('-')
        player.free_throws_made = float(ft_split[0])
        player.free_throws_attempted = float(ft_split[1])
        player.free_throw_pct = self._get_content(cells, 13)

        player.offense_rebounds = self._get_float_content(cells, 14)
        player.defense_rebounds = self._get_float_content(cells, 15)
        player.tr = self._get_float_content(cells, 16)
        player.ast = self._get_float_content(cells, 17)
        player.stl = self._get_float_content(cells, 18)
        player.blk = self._get_float_content(cells, 19)
        player.to = self._get_float_content(cells, 20)
        player.pf = self._get_float_content(cells, 21)
        player.plus_minus = self._get_float_content(cells, 22)
        player.pts = self._get_float_content(cells, 23)

        return player

    def _get_content(self, cells, index):
        cell = cells[index]
        value = cell.contents[0]
        return value

    def _get_int_content(self, cells, index):
        return int(self._get_content(cells, index))

    def _get_float_content(self, cells, index):
        return float(self._get_content(cells, index))

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

    def _get_split_data(self, split_td, delimiter='-'):
        content = self._get_content(split_td)
        parts = content.split(delimiter)
        return parts[0], parts[1]

    @staticmethod
    def get_minutes_float(minutes):
        # expect minutes in string form like '00:00'
        parts = minutes.split(':')
        min_part = int(parts[0])
        sec_part = int(parts[1])
        return min_part + (sec_part/60)
