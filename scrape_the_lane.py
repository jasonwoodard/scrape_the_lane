import requests
import lane_scraper

from bs4 import BeautifulSoup

LOGIN_URL = 'http://drivethelane.com/'
TEAM_URL = 'http://drivethelane.com/team-stats?tid=t1'

USER_NAME = '***REMOVED***'
PASSWORD = '***REMOVED***'

def main():
    # create a session
    session = requests.session()

    # Login
    login_content = login(session, LOGIN_URL, USER_NAME, PASSWORD)
    # print(login_content)

    # Get team content
    team_content = get_page_content(session, TEAM_URL)

    team_soup = get_soup(team_content)
    team_soup.prettify()
    # print(team_soup)

    rows = get_rows(team_soup)

    for row in rows:
        print('---------ROW----------')
        print(row)
    # turn table into CSV


def login(session, url, username, password):
    payload = {'user': username, 'pass': password, 'login' : '1'}
    login_response = session.post(url, data=payload)
    # print(login_response.cookies['vdtl'])
    # print(login_response.cookies['sdtl'])
    return login_response.content

def get_page_content(session, url):
    page = session.get(url)
    return page.content

def get_soup(content):
    # get parse-able version
    soup = BeautifulSoup(content, 'html.parser')
    return soup

def get_rows(soup):
    # pull out table
    rows = soup.select('td > a.player ~ tr')
    return rows

def get_team_name(soup):
    name = soup.find()

if __name__ == '__main__':
    main()