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
    count = 0
    if re.search('Square', option):
        from parsers.square_pharma import square_parser as company_parser
        company_file = 'square_pharma'
        company_name = 'Square Pharmaceuticals Ltd.'
        company_site = 'http://squarepharma.com.bd'
        site_iterables = list(alphabet)
    elif re.search('Incepta', option):
        from parsers.square_pharma import square_parser as company_parser
        company_file = 'incepta_pharma'
        company_name = 'Incepta Pharmaceuticals Ltd.'
        company_site = 'http://inceptapharma.com'
        site_iterables = '' # incepta puts everything on one page
    elif re.search('ACME', option):
        # TODO: doing that in the next commit
        pass
    print('Please wait.')
    print('Data from "{0!s}" will be saved to "{1!s}.json".'.format(
        option, company_file))
    
    count = download_data(
        company_file, company_name, site_iterables, company_site,company_parser)
    
    print('Downloaded {0:d} records from {1!s}'.format(count, option))


def download_data(
    file_name = 'square_pharma',
    company = 'Square Pharmaceuticals Ltd.',
    link_modifiers = list(alphabet),
    website = 'http://squarepharma.com.bd',
    parser = None
    ):
    """Download and store pharmaceutical data from a provider using given parser
    """
    with open('output_data/{!s}.json'.format(file_name), "w") as file_obj:

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
