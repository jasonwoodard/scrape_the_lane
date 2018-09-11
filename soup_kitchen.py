from bs4 import BeautifulSoup

"""
This is a file of helper methods for Beautiful Soup related tasks.

THOUGHTS: THe get_soup function and get_rows function are obviously generalized. The others less so.  Should
they be in the scrapers?
"""

def get_soup(page_content):
    # get parse-able version
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup

# TODO(jw): This needs to be refactored, or at least renamed.
def get_rows(soup, selector):
    # pull out table
    elements = soup.select(selector)
    return elements


def get_team_header(soup):
    element = soup.find(id='team-header')
    return element


def get_info_block_tables(team_page_soup):
    return team_page_soup.select('div.info-block > table')
