import team_object
import soup_kitchen

class TeamScraper(object):

    def __init__(self, team_id, team_page_soup):
        self.team_id = team_id
        self.team_page_soup = team_page_soup

    def get_team(self):
        header = soup_kitchen.get_team_header(self.team_page_soup)
        name = self._get_team_name(header)
        conf_id = self._get_team_conference(header)

        team = team_object.Team()
        team.id = self.team_id
        team.name = name
        team.conference_id = conf_id

        return team

    def _scrape_team_stats(self, team):
        info_blocks = soup_kitchen.get_info_block_tables(self.team_page_soup)
        record, rank, sos = self._get_current_team_stats(info_blocks)
        team.current_season_record = record
        team.current_season_rank = rank
        team.current_season_sos = sos

    @staticmethod
    def _get_team_name(element):
        name_element = element.find('span', {'class': 'h1'})
        return name_element.text

    @staticmethod
    def _get_team_conference(element):
        conf_element = element.find('a', {'class': 'conf'})
        return conf_element.text.lstrip('Conf ')

    @staticmethod
    def _get_current_team_stats(info_block_table):
        # Record Row
        row = rows[0]
        cells = row.contents
        record = cells[2].text

        # Rank Row
        row = rows[1]
        cells = row.contents
        rank = cells[1].text

        # SoS Row
        row = rows[2]
        cells = row.contents
        sos = cells[1].text

        return record, rank, sos,
