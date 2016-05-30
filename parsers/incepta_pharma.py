"""
Parser for Incepta Pharmaceuticals
"""
from bs4 import BeautifulSoup
import requests


def incepta_parser(characters):
    """Parse records from incepta pharma

    Args:
        characters: dumped, used to be compatible with others

    Returns:
        2 item tuple containing all the meds as a list and a count of all meds
    """
    print(characters)
    link = 'http://www.inceptapharma.com/all-products.php'
    meds = parse_char(link)
    return (meds, len(meds))


def parse_char(url):
    """Parse the link for one single character
    Primarily made to make it repeatable."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all("div", {"class": "pitem"})
    records = []

    for item in items:
        med_name = item.find('div', {'class': 'pitem-name'}).text
        med_group = item.find('div', {'class': 'pitem-desc'}).text
        med = {
            'trade_name': med_name,
            'group_name': med_group
        }
        records.append(med)
    return records
