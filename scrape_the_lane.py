import requests
import team_player_scraper

from bs4 import BeautifulSoup

LOGIN_URL = 'http://drivethelane.com/'
TEAM_URL = 'http://drivethelane.com/team-stats?tid=t1'

USER_NAME = '***REMOVED***'
PASSWORD = '***REMOVED***'


def main():
    session = get_session()

    # Get team content
    team_content = get_page_content(session, TEAM_URL)

    scraper = team_player_scraper.TeamPlayerScraper(team_content)
    players = scraper.get_team_player_data()

    for p in players:
        print('------------ROW------------')
        print(p.row)
        print('------------VALUES------------')
        print(p.name, p.year)


def get_page_content(session, url):
    page = session.get(url)
    return page.content


def login(session, url, username, password):
    payload = {'user': username, 'pass': password, 'login': '1'}
    login_response = session.post(url, data=payload)
    return login_response.content


def get_session():
    # create a session
    session = requests.session()
    # Login
    login(session, LOGIN_URL, USER_NAME, PASSWORD)
    return session


if __name__ == '__main__':
    main()
