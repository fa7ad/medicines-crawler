"""
Parser for ACME Laboratories
"""
from bs4 import BeautifulSoup
from random import randint as rand
import requests
import time


def acme_parser(characters):
    """Parse records from acme global

    Args:
        characters: characters to loop through the url

    Returns:
        2 item tuple containing all the meds as a list and a count of all meds
    """
    link = (
        'http://acmeglobal.com/acme/'
        'wp-content/themes/acme/trade_check.php'
        '?initchar_trade={0!s}&divname_trade=human')
    meds = []

    for character in characters:
        try:
            meds += parse_char(link, character)
        except:
            wait = rand(5, 15)
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

    items = soup.find_all("div", {"class": "klasik-pf-text"})
    records = []

    for item in items:
        med_name = item.h3.a.span.text
        med_group = item.find('div', {'class': 'textcontainer'}).text
        med = {
            'trade_name': med_name,
            'group_name': med_group
        }
        records.append(med)
    return records
