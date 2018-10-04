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


def get_content(cells, index):
    cell = cells[index]
    value = cell.contents[0]
    return value


def get_int_content(cells, index):
    content = get_content(cells, index)
    return int(content.replace(',', ''))


def get_float_content(cells, index):
    return float(get_content(cells, index))


def get_split_data(cells, index, delimiter='-'):
    content = get_content(cells, index).replace(',', '')
    parts = content.split(delimiter)
    return parts[0], parts[1]
