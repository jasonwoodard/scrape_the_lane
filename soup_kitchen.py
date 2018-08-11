from bs4 import BeautifulSoup


def get_soup(page_content):
    # get parse-able version
    soup = BeautifulSoup(page_content, 'html.parser')
    return soup


def get_rows(soup, selector):
    # pull out table
    rows = soup.select(selector)
    return rows
