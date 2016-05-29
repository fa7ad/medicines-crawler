#!/usr/bin/env python3
"""
Crawls parmaceutical companies and makes a JSON from all their meds
"""

from string import ascii_uppercase as alphabet
from pick import pick
import json
import re


def main():
    """CLI launcher for the crawler"""
    title = "Choose a pharpaceutical company."
    options = ["Square"]
    indicator = '>>>'
    option, _ = pick(options, title, indicator=indicator)
    if re.search('Square', option):
        from parsers.square_pharma import square_parser as company_parser
        print('Data from "Square" will be recoded to "square_pharma.json".')
        print('Please wait.')
        count = download_data(
            file_name = 'square_pharma',
            company = 'Square Pharmaceuticals Ltd.',
            link_modifiers = list(alphabet),
            website = 'http://squarepharma.com.bd',
            parser = company_parser)
        print('Downloaded {0:d} records from {1!s}'.format(count, option))


def download_data(
    file_name = 'square_pharma',
    company = 'Square Pharmaceuticals Ltd.',
    link_modifiers = list(alphabet),
    website = 'http://squarepharma.com.bd',
    parser=None
    ):
    """Download and store pharmaceutical data from a provider using given parser
    """
    with open('{!s}.json'.format(file_name), "w") as file_obj:

        (company_meds, total) = parser(link_modifiers)
        company = {
            'company': '{!s}'.format(company),
            'website': website,
            'medicine_count': total,
            'medicines': company_meds
        }
        file_obj.write(json.dumps(company, indent=4))
    return len(company_meds)


if __name__ == "__main__":
    main()
