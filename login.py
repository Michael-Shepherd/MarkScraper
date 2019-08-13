import getpass
import requests
from lxml import html

SSO = "https://sso-prod.sun.ac.za/cas/login"

def login(su_id, session):
    '''
    This is a login function for the Stellenbosch university cas SSO
    '''
    login = session.get(SSO)
    login_html = html.fromstring(login.text)
    hidden_elements = login_html.xpath('//form//input[@type="hidden"]')
    form = {x.attrib['name']: x.attrib['value'] for x in hidden_elements}
    form['username'] = su_id
    form['password'] = getpass.getpass()
    session.post(login.url, data=form)
    return logged_in(session)

def logged_in(session):
    resp = session.get(SSO)
    return "Successful" in resp.content