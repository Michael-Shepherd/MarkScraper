#!/usr/bin/env python
import sys
import time
import requests
from functions import get_soup
from login import login
from lxml import html
from bs4 import BeautifulSoup


LOG_IN_URL = 'https://sso-prod.sun.ac.za/cas/login'
MARKS_URL = 'https://web-apps.sun.ac.za/AcademicResults/History.jsp?pLang=1'
GEN_HIST = 'https://web-apps.sun.ac.za/AcademicResults/GenHistPDF.jsp?pLang=1'

###############################################################################
# This function will display the users marks as a table in terminal
# in:
#   session - requests session
# out:
#   Success status
###############################################################################
def get_marks_as_table(session):
    try:
        soup = get_soup(MARKS_URL, session=session)
        rows = soup.find_all('tr')
        for row in rows:
            out = ''
            elements = row.find_all('td')
            for element in elements:
                out += element.text.strip()+ "\t|"
            print(out)
        return True
    except Exception as e:
        return False


###############################################################################
# This function clicks the button on the page that downloads your academic
# history as a pdf into your current directory.
#
# in:
#   session - requests session
# out:
#   Success status
###############################################################################
def download_marks_as_pdf(session):
    try:
        response = session.get(GEN_HIST)
        with open("AcademicHistory.pdf", "wb") as file:
            file.write(response.content)
        return True
    except:
        return False
    


###############################################################################
# Usage: python3 Academic_History.py <SUID> <display(0)/download(1)>
###############################################################################
if __name__ == '__main__':
    args = sys.argv
    if len(args) != 3:
        print(
            'Usage: python3 Academic_History.py <student number>\
        <display(0)/download(1)>'
        )
    else:
        session = requests.Session()
        success = False
        if not login(args[1], session):
            print("Login Failed")
        else:
            if args[2] == '0':
                success = get_marks_as_table(session)
            elif args[2] == '1':
                success = download_marks_as_pdf(session)
                time.sleep(5)
        if success:
            print("Success")
        else:
            print("Failure")