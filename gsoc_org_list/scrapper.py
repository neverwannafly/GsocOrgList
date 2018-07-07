from bs4 import BeautifulSoup
from datetime import datetime
import urllib.request

def scrapper(base_url, start_year, end_year):
    html_content = []
    for year in range(start_year, end_year+1):
        with urllib.request.urlopen(base_url.format(year=year)) as url:
            content = url.read()
            html_file = BeautifulSoup(content, "html.parser")
            html_content.append(html_file)
    return html_content