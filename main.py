import requests
from bs4 import BeautifulSoup

# URL = 'https://sso-prod.sun.ac.za/cas/login?TARGET=http%3A%2F%2Ft2000-05.sun.ac.za%2FEksamenUitslae%2FEksUitslae.jsp%3FpLang%3D1'
URL = 'http://t2000-05.sun.ac.za/EksamenUitslae/EksUitslae.jsp;jsessionid=92e880a930da9645a8f4d5c6429abd668c779bc863f4.e3iQbN0MahmLe3mNb3qTb34NaO0?pLang=1&TARGET=http%3A%2F%2Ft2000-05.sun.ac.za%2FEksamenUitslae%2FEksUitslae.jsp%3FpLang%3D1'

post_values = {'username' : '19059019', 'password' : "Sheep19961"}
response = requests.post(URL, data=post_values)
content = response.content

soup = BeautifulSoup(content)

print(soup)











def login(username, password):
    post_values = {'username' : username, 'password' : password}
    requests.post

def get_content(url):
    response = get(url)
    content = response.content
    return content
