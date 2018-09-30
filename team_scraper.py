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
        team.min = kitchen.get_content(team_stats_cells, 7)

        team.fg = kitchen.get_content(team_stats_cells, 8)
        fg_made, fg_attempt = kitchen.get_split_data(team_stats_cells[8])
        team.fg_made = fg_made
        team.fg_attempted = fg_attempt
        team.fg_pct = kitchen.get_content(team_stats_cells, 9)

        team.three_point = kitchen.get_content(team_stats_cells, 10)
        three_point_made, three_point_attempt = kitchen.get_split_data(team_stats_cells[10])
        team.three_point_made = three_point_made
        team.three_point_attempted = three_point_attempt
        team.three_point_pct = kitchen.get_content(team_stats_cells, 11)

        team.ft = kitchen.get_content(team_stats_cells, 12)
        ft_made, ft_attempt = kitchen.get_split_data(team_stats_cells[12])
        team.ft_made = ft_made
        team.ft_attempted = ft_attempt
        team.ft_pct = kitchen.get_content(team_stats_cells, 13)

        team.oreb = kitchen.get_int_content(team_stats_cells, 14)
        team.dr = kitchen.get_int_content(team_stats_cells, 15)
        team.tr = kitchen.get_int_content(team_stats_cells, 16)
        team.ast = kitchen.get_int_content(team_stats_cells, 17)
        team.blk = kitchen.get_int_content(team_stats_cells, 18)
        team.pf = kitchen.get_int_content(team_stats_cells, 19)
        team.plus_minus = kitchen.get_int_content(team_stats_cells, 20)
        team.pts = kitchen.get_int_content(team_stats_cells, 21)

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
        print(footer_rows)
        team_stats_cells = footer_rows[0].findall('td')
        opponent_stats_cells = footer_rows[1].findall('td')
        return team_stats_cells, opponent_stats_cells,
