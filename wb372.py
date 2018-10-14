import requests
import numpy as np
import csv
import sys
import os
import time
import hashlib
import lxml.html
from functions import *
from bs4 import BeautifulSoup

URL = "http://www.cs.sun.ac.za/wb372/assess/"
DEBUG = 0

def get_marks(url, debug=0):
    soup = get_soup(url, 0)
    table = soup.find("table", {"class":"spreadsheet"})
    table = table.find("tbody")

    if (debug !=0):
        print("Fetched table")

    return table

def gen_csv(soup, debug=0):
    filename = "wb372marks.csv"
    rows = soup.findAll("tr")
    students = []
    with open(os.path.join("marks", filename), "w") as file:
        csv = ""
        for row in rows:
            student = []
            columns = row.findAll("td")
            for col in columns:
                csv += "=" + '"' + col.text+ '"' + ","
                student.append(col.text)
            csv += "\n"
            students.append(student)
        file.write(csv)

    if (debug != 0):
        print("Generated CSV")
    return students

def display_data(data, user_hash,  debug=0):
    Headers = "Hash:\tAss0\tAss1\tAss2\tAss3\tAss4\tAss5\tAss6\tAss7\ttest1\ttest1\ttest1\ttest1\tFinal"
    line = "{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t{}\t"
    average = 0
    final_array = []
    user = ""
    betterthanme=0

    for row in data:
        hash = row[0]
        ass0 = row[1]
        ass1 = row[2]
        ass2 = row[3]
        ass3 = row[4]
        ass4 = row[5]
        ass5 = row[6]
        ass6 = row[7]
        ass7 = row[8]
        test1 = row[9]
        test2 = row[10]
        test3 = row[11]
        test4 = row[12]
        final = row[13]
        final_array.append(float(final))
        average = average + float(final)
        if float(final) > 74.09:
            betterthanme += 1
            print("This Guys is better than me:")
        if hash == user_hash:
            user = line.format("USER", ass0, ass1, ass2, ass3, ass4, ass5, ass6, ass7,\
                              test1, test2, test3, test4,\
                              final)
        print(line.format(hash, ass0, ass1, ass2, ass3, ass4, ass5, ass6, ass7,\
                          test1, test2, test3, test4,\
                          final))


    print("*****\n{}\n*****".format(user))
    average = average/len(data)
    print("Average: {:.2f}".format(average))
    print("{} out of {} are better than me".format(betterthanme, len(data)))

    final = np.asarray(final_array)


    if debug != 0:
        print("displayed data")
################################################################################
#
# Usage:
# wb372 [debug] [student number] [First year registered] [Birthday(yyyy-mm-dd)]
#
################################################################################
if __name__ == "__main__":
    args = sys.argv
    student_number = "12345678"
    year = "1234"
    birthday = "1234-56-78"
    print("Usage: python3 wb372 [debug] [student number]\
 [First year registered] [Birthday(yyyy-mm-dd)]")
    print(len(args))
    if len(args) > 1:
        DEBUG = args[1]
    if len(args) > 2:
        print(args[2])
        student_number = args[2]
    if len(args) > 3:
        year = args[3]
    if len(args) > 4:
        birthday = args[4]

    hash = student_number+"-"+year+"-"+birthday
    hash = hashlib.sha1(hash.encode('utf-8')).hexdigest()[:5]

    soup = get_marks(URL, DEBUG)
    data = gen_csv(soup, DEBUG)
    display_data(data, hash, DEBUG)
