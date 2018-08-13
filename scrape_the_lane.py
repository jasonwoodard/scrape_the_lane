import requests

import data_exporter
import team_player_scraper
import pprint
from argparse import ArgumentParser


LOGIN_URL = 'http://drivethelane.com/'
TEAM_URL = 'http://drivethelane.com/team-stats?tid=t1'

pp = pprint.PrettyPrinter()

def main(args):

    session = get_session(args.username, args.password)

    # Get team content
    team_content = get_page_content(session, TEAM_URL)

    scraper = team_player_scraper.TeamPlayerScraper(team_content)
    players = scraper.get_team_player_data()

    # for p in players:
        # print('------------ROW------------')
        # print(p.row)
        # print('------------VALUES------------')
        # pp.pprint(p)

    value = {'rows': players}
    exporter = data_exporter.DataExporter()
    exporter.export_to_csv(players[0].row_template, value)


def get_page_content(session, url):
    page = session.get(url)
    return page.content


def login(session, url, username, password):
    payload = {'user': username, 'pass': password, 'login': '1'}
    login_response = session.post(url, data=payload)
    return login_response.content


def get_session(username, password):
    # create a session
    session = requests.session()
    # Login
    login(session, LOGIN_URL, username, password)
    return session


parser = ArgumentParser()
parser.add_argument("-u", "--user", dest="username", default=True,
                    help="You need to provide a username")
parser.add_argument("-p", "--pass", dest="password", default=True,
                    help="You need to provide a password")

args = parser.parse_args()

if __name__ == '__main__':
    main(args)
