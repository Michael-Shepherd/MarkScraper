from selenium import webdriver
import sys
import time

LOG_IN_URL = 'https://sso-prod.sun.ac.za/cas/login?service=https%3A%2F%2Flearn\
.sun.ac.za%2Flogin%2Findex.php'

MARKS_URL = 'https://web-apps.sun.ac.za/AcademicResults/History.jsp?pLang=1'

FORM_DATA = {"username":'username',\
            "password":'password',\
            "lt":'LT-5687877-12jGFj5yx6miSpVtTnJDAg5jA6jIq1',\
            "execution":'e1s1',\
            "_eventId":'submit'}

###############################################################################
# This function will open a chromium browser onto the Academic_History page
# of Stellenbosch university, given that you have entered a correct student
# number and password.
#
# Require: chromedriver in PATH
#
# in:
#   driver - the current webdriver
# out:
#   driver - the updated webdriver
###############################################################################
def open_academic_history(driver):
    driver.get(MARKS_URL)
    username_box = driver.find_element_by_id('username')
    password_box = driver.find_element_by_id('password')
    login_button = driver.find_element_by_xpath("//input[@type='submit']")
    time.sleep(1)
    username_box.send_keys(FORM_DATA['username'])
    password_box.send_keys(FORM_DATA['password'])
    print('Username and Password inserted')
    login_button.click()
    print('Login button clicked')
    return driver

def get_marks_as_table(driver):
    rows = driver.find_elements_by_xpath("//table/tbody/tr")
    for row in rows:
        print(row.text)
    return driver

###############################################################################
# This function clicks the button on the page that downloads your academic
# history as a pdf into your default downloads folder.
# 
# in:
#   driver - the current webdriver
# out:
#   driver - the updated webdriver
###############################################################################
def download_marks_as_pdf(driver):
    driver.find_element_by_xpath("//input[@type='submit']").click()
    return driver

###############################################################################
# Usage: python3 Academic_History.py
#        <student number>
#        <su password>
#        <display(0)/download(1)>
###############################################################################
if __name__ == "__main__":
    args = sys.argv
    if len(args) != 4:
        print('Usage: python3 Academic_History.py <student number>\
        <su password> <display(0)/download(1)>')
    else:
        FORM_DATA['username'] = args[1]
        FORM_DATA['password'] = args[2]
        option = webdriver.ChromeOptions()
        option.add_argument('-incognito')
        driver = webdriver.Chrome(chrome_options=option)
        open_academic_history(driver)
        if args[3] == '0':
            get_marks_as_table(driver)
        else:
            download_marks_as_pdf(driver)
            time.sleep(5)
        driver.quit()
