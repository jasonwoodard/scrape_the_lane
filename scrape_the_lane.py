import requests

from data_exporter import DataExporter
import team_player_scraper
from argparse import ArgumentParser

from player_object import Player
from team_object import Team

LOGIN_URL = 'http://drivethelane.com/'

TEAM_URL = 'http://drivethelane.com/team-stats?atype=t&gtype=reg&mode=g&tid=t{0}'
# THIS URL IS FOR THE AVERAGES PAGE IF YOU WANT TO SCRAPE IT: TEAM_URL = 'http://drivethelane.com/team-stats?tid=t{0}'


def main(args):
    """
    Main method that kicks off whole scrape and export.

    :param args:  parsed arguments object for getting command line parameters
    :return: None
    """

    print('-----------------------\nBeginning scrape\n-----------------------')

    # Get session logged in session object
    session = get_session(args.username, args.password)

    # Define array for the player objects we're going to scrape.
    players = []
    teams = []

    # Define a team_id_counter counter to fetch teams by id to scrape the players.
    team_id_counter = 0
    while team_id_counter < 256:  # maximum team id is 256
        # Advance the team id counter so the first one is 1 and the last will be 256.
        team_id_counter += 1

        # Get team content
        team_content = get_page_content(session, build_team_url(team_id_counter))

        # Instantiate a TeamPlayerScraper object to parse the team page content.
        scraper = team_player_scraper.TeamPlayerScraper(team_content, team_id_counter)

        # Get array of players for current team_id. Id was passed in above.
        team_players = scraper.get_team_player_data()

        # Add the players from this team
        players.extend(team_players)

        # Grab the team off the first player and add to teams array.
        teams.append(team_players[0].team)

        # Print a summary of the results of the team scrape to console to monitor progress.
        print('Team Id: {0}'.format(team_id_counter))
        print('Team {0} Players: {1} '.format(team_id_counter, len(team_players)))
        print('Total Players: {0}'.format(len(players)))

    print('Scrape complete.\n-----------------------\n Starting export to CSV')
    # Instantiate a data exporter object and write to CSV.
    exporter = DataExporter()
    exporter.file_prefix = 'players-'
    exporter.write_to_csv(Player.RowHeader, players)

    exporter.file_prefix = 'teams-'
    exporter.write_to_csv(Team.RowHeader, teams)

    print('Export to CSV complete.')
    print('Script complete.\n-----------------------')


def build_team_url(team_id):
    """
    Builds the team URL from the URL constant

    :param team_id: team id
    :return: team specific url
    """
    return TEAM_URL.format(team_id)


def get_page_content(session, url):
    """
    Fetches page content for scraping.

    :param session: logged in session.
    :param url: url to return content for.
    :return: returns raw page content from url.
    """
    page = session.get(url)
    print('Scrape Request: {0} from url: {1}'.format(page.status_code, url))
    return page.content


def login(session, url, username, password):
    """
    Logs into drivethelane.com using the session, url, and credentials provided

    :param session: request library session object where cookies, etc will be.
    :param url: login url
    :param username: drivetheland.com username.
    :param password: password for username.
    :return: returns login page response content
    """
    payload = {'user': username, 'pass': password, 'login': '1'}
    login_response = session.post(url, data=payload)
    print('Login Request: {0} username: {1}'.format(
        login_response.status_code, username))
    return login_response.content


def get_session(username, password):
    """
    Creates server session where authentication cookie is kept allowing access to pages requiring login.

    :param username: drivethelane.com username.
    :param password: password for username.
    :return: logged in session.
    """
    # create a session
    session = requests.session()
    # Login
    login(session, LOGIN_URL, username, password)
    return session


parser = ArgumentParser()
parser.add_argument('-u', '--user', dest='username',
                    help='You need to provide a username')
parser.add_argument('-p', '--pass', dest='password',
                    help='You need to provide a password')
# parser.add_argument('-d', '--debug', dest='debug', default=False)

cmd_args = parser.parse_args()

if __name__ == '__main__':
    main(cmd_args)
