#!/usr/bin/env python3
"""
Crawls Square pharma and makes a JSON from all their meds
"""

from string import ascii_uppercase as alphabet
from bs4 import BeautifulSoup
from requests import get as http_get


def crawl(characters):
    """
    Makes a JSON file of all the medicines from Square

    Args:
        characters: list of characters to search in square's database

    Returns:
        A two item tuple of output formatted strings and total number of meds
    """
    output = "Square Pharmaceuticals Ltd.\n"
    total = 0

    # Create an object of file
    with open('square_pharma.json', "w") as file_obj:
        file_obj.write('{')
        # write metadata
        file_obj.write('''"meta": {
                "company": "Square Pharmaceuticals Ltd."
            },''')

        # make the medicines object
        file_obj.write('"medicines": [')

        output += """
        Company \t Brand Name \t Group
        ======================================"""

        url = "http://squarepharma.com.bd/products-by-tradename.php?type=trade&char="
        for character in characters:
            url += character

            # Get the requested URL
            req = http_get(url)

            # Passing the requested content to Beautiful Soup
            soup = BeautifulSoup(req.content, 'html.parser')

            # Targeting data/html content
            items = soup.find_all("div", {"class":"products-holder"})
            total += len(items)


            for item in items:
                med_name = item.contents[2].text
                med_group = item.contents[4].text

                output_line = "Square \t " + med_name + " \t " + med_group
                output += output_line

                #write meds to json
                file_obj.write('''{
                        "trade_name": "%s",
                        "group_name": "%s"
                    },''' % (med_name.encode('utf-8'), med_group.encode('utf-8')))

        file_obj.write(']}')
    return (output, total)


if __name__ == "__main__":
    (CRAWL_RESULT, COUNT) = crawl(list(alphabet))
    print(CRAWL_RESULT)
    print("Total number of meds:", COUNT)
