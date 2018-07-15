import requests
import csv
import arrow
from bs4 import BeautifulSoup

# URL = 'http://t2000-05.sun.ac.za/EksamenUitslae/EksUitslae.jsp;jsessionid=92e880a930da9645a8f4d5c6429abd668c779bc863f4.e3iQbN0MahmLe3mNb3qTb34NaO0?pLang=1&TARGET=http%3A%2F%2Ft2000-05.sun.ac.za%2FEksamenUitslae%2FEksUitslae.jsp%3FpLang%3D1'
URL = 'http://t2000-05.sun.ac.za/EksamenUitslae/EksUitslae.jsp?pLang=1'
def get_soup(URL, username="19059019", password="Sheep19962"):
	try:
		post_values = {'username' : username, 'password' : password}
		response = requests.post(URL, data=post_values)
		content = response.content
		return BeautifulSoup(content, "html.parser")
	except:
		return("CONNECTION ERROR")

def save_marks(soup):
	filename = arrow.now().format("DDMMYYHHmm") + ".csv"
	table = soup.find_all("table")[1]
	print(soup)
	rows = table.find_all("tr")
	del rows[0]

	for row in rows:
		cols = row.find_all("td")
		for col in cols:
			if not col.find("img"):
				print(col.text)
			else:
				print()
		print()


if __name__ == "__main__":
	soup = get_soup(URL)
	save_marks(soup)
