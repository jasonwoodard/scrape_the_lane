import requests

from data_exporter import DataExporter
import team_player_scraper
import pprint
from argparse import ArgumentParser

from player_object import Player

LOGIN_URL = 'http://drivethelane.com/'
TEAM_URL = 'http://drivethelane.com/team-stats?tid=t1'

pp = pprint.PrettyPrinter()

def main(args):
    print '-----------------------\nBeginning scrape\n-----------------------'
    session = get_session(args.username, args.password)

    # Get team content
    team_content = get_page_content(session, TEAM_URL)

    scraper = team_player_scraper.TeamPlayerScraper(team_content)
    players = scraper.get_team_player_data()

    print 'Scraped Players: {0}'.format(len(players))

    # Debug Loop used to debug output
    # for p in players:
        # print ('------------ROW------------')
        # print(p.row)
        # print('------------VALUES------------')
        # print p.name

    exporter = DataExporter()
    exporter.export_to_csv(Player.RowTemplate, players)


def get_page_content(session, url):
    page = session.get(url)
    print 'Scrape Request: {0} from url: {1}'.format(page.status_code, url)
    return page.content


def login(session, url, username, password):
    payload = {'user': username, 'pass': password, 'login': '1'}
    login_response = session.post(url, data=payload)
    print 'Login Request: {0} username: {1}'.format(
        login_response.status_code, username)
    return login_response.content


def get_session(username, password):
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
parser.add_argument('-d', '--debug', dest='debug', default=False)

args = parser.parse_args()

if __name__ == '__main__':
    main(args)
