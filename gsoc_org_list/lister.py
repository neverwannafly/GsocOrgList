import sys

from .scrapper import scrapper
from operator import itemgetter

class Lister:

    def __init__(self):
        self._get_list()

    BASE_URLS = {
        "2009-2015": "https://www.google-melange.com/archive/gsoc/{year}",
        "2016-2017": "https://summerofcode.withgoogle.com/archive/{year}/organizations/",
        # "2018-2018": "https://summerofcode.withgoogle.com/organizations/",
    }
    ORGANISATIONS = {}

    def _get_list(self):
        for years in self.BASE_URLS:
            int_years = [int(year) for year in years.split('-')]
            start_year = int_years[0]
            end_year = int_years[1]
            url = self.BASE_URLS[years]
            content = scrapper(url, start_year, end_year)
            for iteration, soup_object in enumerate(content):
                if start_year==2009:
                    organisations = soup_object.find_all('a')
                    for index in range(19, len(organisations)-4):
                        if self.ORGANISATIONS.get(organisations[index].get_text().lower(), None):
                            self.ORGANISATIONS[organisations[index].get_text().lower()] += 1
                        else:
                            self.ORGANISATIONS[organisations[index].get_text().lower()] = 1
                elif start_year==2016:
                    organisations = soup_object.find_all('h4', class_="organization-card__name")
                    for index in range(0, len(organisations)-1):
                        if self.ORGANISATIONS.get(organisations[index].get_text().lower(), None):
                            self.ORGANISATIONS[organisations[index].get_text().lower()] += 1
                        else:
                            self.ORGANISATIONS[organisations[index].get_text().lower()] = 1

    def _print_headers(self):
        print("|------------------------------------------------------------------------------------------------------------------|")
        print("|                Organisations                                                                         | Frequency |")
        print("|__________________________________________________________________________________________________________________|")

    def _print_footers(self):
        print("|------------------------------------------------------------------------------------------------------------------|")

    def _parse_dictionary(self):
        self.ORGANISATIONS = sorted(self.ORGANISATIONS.items(), key=itemgetter(1), reverse=True)
        self._print_headers()
        for organisation in self.ORGANISATIONS:
            print("| {0: >2}{1: <99}".format("", organisation[0])+ "|" + "{0: >5}{1: <6}".format("",organisation[1]) + "|")
        self._print_footers()

    def get_organisations(self):
        self._parse_dictionary()