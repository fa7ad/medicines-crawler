"""
Parser for square pharmaceuticals
"""
from bs4 import BeautifulSoup
import requests


def square_parser(characters):
    """Parse records from square pharma

    Args:
        characters: characters to loop through the url
    
    Returns:
        2 item tuple containing all the meds as a list and a count of all meds
    """
    link = 'http://squarepharma.com.bd/products-by-tradename.php?type=trade&char={0!s}'
    meds = []

    for character in characters:
        url = link.format(character)
        response = requests.get(url)
        soup = BeautifulSoup(response.content, 'html.parser')

        items = soup.find_all("div", {"class": "products-holder"})

        for item in items:
            med_name = item.contents[2].text
            med_group = item.contents[4].text
            med = {
                'trade_name': med_name,
                'group_name': med_group
            }
            meds.append(med)

    return (meds, len(meds))
