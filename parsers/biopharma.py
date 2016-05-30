"""
Parser for BIOPHARMA
"""
from bs4 import BeautifulSoup
import requests


def biopharma_parser(characters):
    """Parse records from incepta pharma

    Args:
        characters: dumped, used to be compatible with others

    Returns:
        2 item tuple containing all the meds as a list and a count of all meds
    """
    print(characters)
    link = 'http://www.biopharmabd.com/pharma/products/product.php?short=1'
    meds = parse_char(link)
    return (meds, len(meds))


def parse_char(url):
    """Parse the link for one single character
    Primarily made to make it repeatable."""
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all("tr", {"style": (
        "background-color:#FBEDF3;"
        "line-height:40px;font-weight:normal;"
        "font-size:11px;vertical-align:middle;")})
    records = []

    for item in items:
        med_name = item.contents[1].span.text
        med_group = item.contents[3].span.text
        med = {
            'trade_name': med_name,
            'group_name': med_group
        }
        records.append(med)
    return records
