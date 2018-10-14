import requests
import csv
import sys
import arrow
import os
import time
import lxml.html
from bs4 import BeautifulSoup

# URL = 'https://sso-prod.sun.ac.za/cas/login?TARGET=http%3A%2F%2Ft2000-05.sun.ac.za%2FEksamenUitslae%2FEksUitslae.jsp%3FpLang%3D1'
URL = 'https://web-apps.sun.ac.za/AcademicResults/'
DEBUG = 0

def get_soup(URL, username, password, debug=0):
	try:
		with requests.session() as session:
			time.sleep(0.05)
			content = lxml.html.fromstring(session.get(URL).text)
			hidden_elements = content.xpath('//form//input[@type="hidden"]')
			post_values = {element.attrib['name']: element.attrib['value'] for element in hidden_elements}
			post_values['username'] =  username
			post_values['password'] =  password
			print(post_values)

			time.sleep(0.01)
			content = session.post(URL, data=post_values)

			if (content.url != URL):
				return BeautifulSoup(content.content, "lxml")
			else:
				return("CONNECTION ERROR")
	except:
		return("CONNECTION ERROR")

# def save_marks(soup, debug=0):
# 	filename = sys.argv[1]+ "_" + arrow.now().format("DDMMYYHHmm") + ".csv"
# 	file = open(os.path.join("marks", filename), "w+")
# 	csv = ""
#
# 	table = soup.find_all("table")[1]
# 	rows = table.find_all("tr")
# 	del rows[0]
#
# 	for row in rows:
# 		cols = row.find_all("td")
# 		for col in cols:
# 			if not col.find("img"):
# 				csv += col.text + ','
# 			else:
# 				csv += '-,'
# 		csv += ",\n"
#
# 	file.write(csv)
#
# 	if debug != 0:
# 		print(csv)


if __name__ == "__main__":
    soup = ''
    if len(sys.argv) < 3:
        print("Usage: python3 main.py <username> <password> [DEBUG]")
    else:
        if len(sys.argv) > 3:
            DEBUG = int(sys.argv[3])
        soup = get_soup(URL, sys.argv[1], sys.argv[2], DEBUG)
    print(soup)
