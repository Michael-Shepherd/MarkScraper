import requests
import csv
import time
import sys
import arrow
import os
import lxml.html
from bs4 import BeautifulSoup
from socket import error as SocketError

URL = 'https://web-apps.sun.ac.za/AcademicResults/'

def get_url(url):
    for i in range (3):
        with requests.session() as session:
            try:
                time.sleep(0.01)
                request = session.get(url)
                return BeautifulSoup(request.content, "lxml")
            except:
                print("\nAttempt: %d\n"%i)
    return(False)

print(get_url(URL))
