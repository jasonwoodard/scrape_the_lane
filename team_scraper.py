import team_object
import soup_kitchen as kitchen


class TeamScraper(object):

    def __init__(self, team_id, team_page_soup):
        self.team_id = team_id
        self.team_page_soup = team_page_soup

    def get_team(self):
        header = kitchen.get_team_header(self.team_page_soup)
        name = self._get_team_name(header)
        conf_id = self._get_team_conference(header)

        team = team_object.Team()
        team.id = self.team_id
        team.name = name
        team.conference_id = conf_id

        team_stats_cells, opponent_stats_cells = self._scrape_team_totals_rows(self.team_page_soup)

        # Cells 0 - 5 are labels and empty
        team.gms = kitchen.get_int_content(team_stats_cells, 6)
        team.minutes = kitchen.get_content(team_stats_cells, 7)
        team.minutes_float = self.get_minutes_float(team.minutes)

        team.fg = kitchen.get_content(team_stats_cells, 8)
        fg_made, fg_attempt = kitchen.get_split_data(team_stats_cells, 8)
        team.fg_made = fg_made
        team.fg_attempted = fg_attempt
        team.fg_pct = kitchen.get_content(team_stats_cells, 9)

        team.three_point = kitchen.get_content(team_stats_cells, 10)
        three_point_made, three_point_attempt = kitchen.get_split_data(team_stats_cells, 10)
        team.three_point_made = three_point_made
        team.three_point_attempted = three_point_attempt
        team.three_point_pct = kitchen.get_content(team_stats_cells, 11)

        team.ft = kitchen.get_content(team_stats_cells, 12)
        ft_made, ft_attempt = kitchen.get_split_data(team_stats_cells, 12)
        team.ft_made = ft_made
        team.ft_attempted = ft_attempt
        team.ft_pct = kitchen.get_content(team_stats_cells, 13)

        team.oreb = kitchen.get_int_content(team_stats_cells, 14)
        team.dr = kitchen.get_int_content(team_stats_cells, 15)
        team.tr = kitchen.get_int_content(team_stats_cells, 16)
        team.ast = kitchen.get_int_content(team_stats_cells, 17)
        team.stl = kitchen.get_int_content(team_stats_cells, 18)
        team.blk = kitchen.get_int_content(team_stats_cells, 19)
        team.to = kitchen.get_int_content(team_stats_cells, 20)
        team.pf = kitchen.get_int_content(team_stats_cells, 21)
        team.plus_minus = kitchen.get_int_content(team_stats_cells, 22)
        team.pts = kitchen.get_int_content(team_stats_cells, 23)

        # ADDING OPPONENT ROW FROM SITE
        # Cells 0 - 5 are labels and empty
        team.opp_gms = kitchen.get_int_content(opponent_stats_cells, 6)
        team.opp_minutes = kitchen.get_content(opponent_stats_cells, 7)
        team.opp_minutes_float = self.get_minutes_float(team.opp_minutes)

        team.opp_fg = kitchen.get_content(opponent_stats_cells, 8)
        opp_fg_made, opp_fg_attempt = kitchen.get_split_data(opponent_stats_cells, 8)
        team.opp_fg_made = opp_fg_made
        team.opp_fg_attempted = opp_fg_attempt
        team.opp_fg_pct = kitchen.get_content(opponent_stats_cells, 9)

        team.opp_three_point = kitchen.get_content(opponent_stats_cells, 10)
        opp_three_point_made, opp_three_point_attempt = kitchen.get_split_data(opponent_stats_cells, 10)
        team.opp_three_point_made = opp_three_point_made
        team.opp_three_point_attempted = opp_three_point_attempt
        team.opp_three_point_pct = kitchen.get_content(opponent_stats_cells, 11)

        team.opp_ft = kitchen.get_content(opponent_stats_cells, 12)
        opp_ft_made, opp_ft_attempt = kitchen.get_split_data(opponent_stats_cells, 12)
        team.opp_ft_made = opp_ft_made
        team.opp_ft_attempted = opp_ft_attempt
        team.opp_ft_pct = kitchen.get_content(opponent_stats_cells, 13)

        team.opp_oreb = kitchen.get_int_content(opponent_stats_cells, 14)
        team.opp_dr = kitchen.get_int_content(opponent_stats_cells, 15)
        team.opp_tr = kitchen.get_int_content(opponent_stats_cells, 16)
        team.opp_ast = kitchen.get_int_content(opponent_stats_cells, 17)
        team.opp_stl = kitchen.get_int_content(opponent_stats_cells, 18)
        team.opp_blk = kitchen.get_int_content(opponent_stats_cells, 19)
        team.opp_to = kitchen.get_int_content(opponent_stats_cells, 20)
        team.opp_pf = kitchen.get_int_content(opponent_stats_cells, 21)
        team.opp_plus_minus = kitchen.get_int_content(opponent_stats_cells, 22)
        team.opp_pts = kitchen.get_int_content(opponent_stats_cells, 23)

        return team

    @staticmethod
    def _get_team_name(element):
        name_element = element.find('span', {'class': 'h1'})
        return name_element.text

    @staticmethod
    def _get_team_conference(element):
        conf_element = element.find('a', {'class': 'conf'})
        return conf_element.text.lstrip('Conf ')

    @staticmethod
    def _scrape_team_totals_rows(team_soup):
        footer_rows = team_soup.select('#team-stats tfoot tr')

        # row 0 is just a spacer.
        team_stats_cells = footer_rows[1].find_all('td')
        opponent_stats_cells = footer_rows[2].find_all('td')
        return team_stats_cells, opponent_stats_cells,

    @classmethod
    def get_minutes_float(cls, minutes):
        # expect minutes in string form like '00:00'
        parts = minutes.split(':')
        min_part = int(parts[0])
        sec_part = int(parts[1])
        return min_part + (sec_part / 60)
