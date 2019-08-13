import requests
import time
import lxml.html
from bs4 import BeautifulSoup

###############################################################################
# Gets the Beuatiful Soup of the content of a url, using the Requests and bs4
# packages.
#
# If the first request fails, there will be two more attwmpt before EMPTY is
# returned.
#
# in:
#   url - url of required webpage
#   debug - debug value
# out:
#   Either "EMPTY" or the soup of the given url
###############################################################################
def get_soup(url, debug=0, session=None):
    if session == None:
        session = requests.session()
    for i in range (3):
        try:
            time.sleep(0.01)
            request = session.get(url)
            return BeautifulSoup(request.content, "lxml")
        except:
            if debug != 0:
                print("\nAttempt: %d\n"%i)
            else:
                pass
    return("EMPTY")
