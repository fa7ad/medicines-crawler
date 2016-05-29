"""
Parser for square pharmaceuticals
"""
from bs4 import BeautifulSoup
from random import randint as rand
import requests
import time



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
        try:
            meds += parse_char(link, character)
        except:
            wait = rand(5,15)
            print('Failed on character {!s}.'.format(character))
            print('Trying again in {0:d}s.'.format(wait))
            time.sleep(wait)
            try:
                meds += parse_char(link, character)
            except:
                print('Failed on character {!s} again.'.format(character))
                print('Skipping character.')

    return (meds, len(meds))


def parse_char(link, character):
    """Parse the link for one single character
    Primarily made to make it repeatable."""
    url = link.format(character)
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    items = soup.find_all("div", {"class": "products-holder"})
    records = []

    for item in items:
        med_name = item.contents[2].text
        med_group = item.contents[4].text
        med = {
            'trade_name': med_name,
            'group_name': med_group
        }
        records.append(med)
    return records