import soup_kitchen as kitchen
import schedule_object


class TeamScheduleScraper:
    def __init__(self, schedule_page, team_id):
        self.schedule_page_soup = kitchen.get_soup(schedule_page)
        self.team_id = team_id

    def get_schedule_game_data(self):
        games = []

        schedule_scraper = ScheduleScraper(self.team_id, self.schedule_page_soup,)
        schedule = schedule_scraper.get_team()

        rows = self._get_schedule_rows()
        for row in rows:
            schedule = self._extract_schedule_row(row)
            schedule.team = team
            players.append(player)

        return players

    def _get_schedule_rows(self):
        return self.team_page_soup.select('hl-gray, hl-gray conf')

    def _extract_schedule_row(self, row):
        # Attach row to player object incase we need it later.
        schedule = schedule_object.Schedule()

        cells = row.find_all('td')

        # Extract data from cells (TDs) by cell ID and populate the player object.
        # RISK: If the order of the cells changes, we need to revise this section.


        # schedule.id = self._get_schedule_id(cells[0]) NOTE: We need to grab this from the team banner.



        schedule.game_number = kitchen.get_content(cells, 0)
        schedule.date = kitchen.get_content(cells, 1)
        # Cell [2] is blank.
        schedule.opp_PR = kitchen.get_content(cells, 3)
        schedule.opp_name = kitchen.get_content(cells, 4)

        # Need to split record into wins and losses.
        opp_record = kitchen.get_content(cells, 5)
        opp_record_split = opp_record.split('-')
        schedule.opp_wins = int(opp_record_split[0])
        schedule.opp_losses = int(opp_record_split[1])

        schedule.opp_coach = kitchen.get_content(cells, 6)

        # Need to split all_score into "W or L", Team Points, Opp Points
        all_score = kitchen.get_content(cells, 7)
        all_score_split = all_score.split(" ")
        schedule.w_or_l = all_score_split[0]
        schedule.score = int(all_score_split[1])
        schedule.opp_score = int(all_score_split[3])

        # Cell [8] is the play by play URL link.

        # Must split record into wins, losses, conf wins and conf losses
        record = kitchen.get_content(cells, 9)
        schedule.wins = kitchen.get_content(cells, 9)
        schedule.losses = kitchen.get_content(cells, 9)
        schedule.conf_wins = kitchen.get_content(cells, 9)
        schedule.conf_losses = kitchen.get_content(cells, 9)

        # Must split settings into tempo, defense, three point settings
        settings = kitchen.get_content(cells, 10)
        settings_split = settings.split('/')
        schedule.tempo = settings_split[0]
        schedule.defense = settings_split[1]
        schedule.three_point_shooting = settings_split[2]
        return schedule

    @staticmethod
    def _get_win_loss_record(win_loss_value):
        """
        Takes win loss string in format 'a - b' or 'a - b (c - d)' and returns a 4 int|None tuple of the result.
        :param win_loss_value: Raw string value from win loss column on schedule page
        :return: 4 int|None tuple of wins, losses, ???, ???
        """
        # Assuming value values are 'a - b' or 'a - b (c - d)', rather than fight the format take steps to make it
        # something we can work with.
        # Steps:
        # 1) replace the open paren if present with a '- ' (dash space).
        # 2) remove the closing paren if present.
        #
        # If the input is 'a - b' all this has no effect. If the input is 'a - b (c - d)' the steps do the following
        # Result #1) 'a - b (c - d)' => 'a - b - c - d)'
        # Result #2) 'a - b - c - d)' => 'a - b - c - d'
        # And now, we have an ordered list of values that easily split on ' - ' (dash space dash).
        re_delimited = win_loss_value.replace('(', '- ').replace(')', '')

        as_list = re_delimited.split(' - ')

        # Here we use fancy python list comprehension to turn all the string values into ints: int('1') = 1
        int_list = [int(i) for i in as_list]

        # We're expecting a tuple length 4 as the output, in the case of 'a - b' input we're 2 short. So pad the end
        # of the list with two 'None' values.
        if len(int_list) == 2:
            int_list.extend([None, None])

        # Finally, convert the list to a tuple - could you use a list (array) instead, yeah you could but isn't it nice
        # to stretch yourself and use some of the cooler parts of Python?
        return tuple(int_list)

# NOTE: STILL NEED TO UPDATE FUNCTIONS BELOW FOR SCHEDULE SCRAPER

    @staticmethod
    def _get_player_name(name_td):
        # <a href="player?pid=p9DE5067489" class="player">Joseph Piccione</a>
        return name_td.find('a').text

    @staticmethod
    def _get_player_id(name_td):
        # <a href="player?pid=p9DE5067489" class="player">Joseph Piccione</a>
        href = name_td.find('a')['href']
        # href should be 'player?pid=p9DE5067489'
        # use regular expression to match part after equals sign.
        matches = re.search(r'pid=(p\w+)', href)
        # if a match is found return value otherwise return -1
        return matches.group(1) if matches else -1