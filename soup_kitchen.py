from bs4 import BeautifulSoup


def get_soup(page_content):
    # get parse-able version
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup


def get_rows(soup, selector):
    # pull out table
    elements = soup.select(selector)
    return elements


def get_team_header(soup):
    element = soup.find(id='team-header')
    return element
