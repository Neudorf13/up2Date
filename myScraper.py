import re

from bs4 import BeautifulSoup
import requests


def scrapePython():

    page = requests.get("https://www.python.org/downloads/")
    soup = BeautifulSoup(page.text, "html.parser")

    ol_tag = soup.find('ol', class_='list-row-container menu')

    if ol_tag:

        first_li_tag = ol_tag.find('li')
        if first_li_tag:
            data = first_li_tag.get_text(strip=True)
            print(data)
            return data
            # formatPython(data)
        else:
            return None
    else:
        print("Could not find the specified <ol> tag with class 'list-row-container menu'.")
        return None


def formatPython(data):
    versionNumber = ""
    matchVersion = re.match(r'^([^a-zA-Z]+)', data)
    if matchVersion:
        versionNumber = matchVersion.group(1)
        print(versionNumber)

    releaseDate = ""
    matchReleaseDate = re.search(r'(\d{4}-\d{2}-\d{2})', data)
    if matchReleaseDate:
        releaseDate = matchReleaseDate.group(1)
        print(releaseDate)

    if versionNumber and releaseDate:
        return versionNumber + " " + releaseDate
    else:
        return None


def scrapeJava():
    print("hello?")
    page = requests.get("https://www.java.com/releases/")
    soup = BeautifulSoup(page.text, "html.parser")

    tablesDiv = soup.find('div', class_='tables')

    if tablesDiv:
        print("tables!")

    # released_tbody = soup.find('tbody', id='released')
    # if released_tbody:
    #     # Extract data from the <tbody> element
    #     print("something")
    #     data = released_tbody.get_text(strip=True)
    #     print(data)
    #     return data
    # else:
    #     print("nota")
    #     return None


def scrapeRuby():
    page = requests.get("https://www.ruby-lang.org/en/downloads/releases/")
    soup = BeautifulSoup(page.text, "html.parser")

    tablesDiv = soup.find('table', class_='release-list')

    if tablesDiv:
        print("RUBY!!!")
        tr_tags = tablesDiv.find_all('tr')
        if len(tr_tags) >= 2:
            second_tr_tag = tr_tags[1]
            td_tags = second_tr_tag.find_all('td')
            data1 = td_tags[0].get_text(strip=True)
            data2 = td_tags[1].get_text(strip=True)
            # print(data1)
            data1 = data1.split(' ')[1]
            print(data1)
            print(data2)
            return data1 + " " + data2








