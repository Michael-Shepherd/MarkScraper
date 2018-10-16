# MarkScraper
Python web scraper to fetch marks from my university website.

## wb372 Marks

This is a function that will fetch the 2018 wb372 marks. The marks will be
displayed in terminal, as well as be inserted into a csv. This will probably
not work for any other year, due to the hash function used for privacy of
marks.

This can be executed with the following code
```
python3 wb372.py [debug] [student number] [first year of registration] [birthday(yyyy-mm-dd)]
```

The debug argument can be used on its own, but in order to correctly find your
own marks, all of the other arguments must be filled in correctly.

The *display_data* function also shows you how many people are better than me,
just incase anyone was wondering.

## Academic history

This is a function that will fetch the full up to date academic history of any
student at Stellenbosch University. This academic history is not t be used as
an official document.

The function can either display Academic History in the terminal, or it can
download them in pdf format into your default download folder, using the
following command
```
Usage: python3 Academic_History.py <student number> <su password> <display(0)/download(1)>
```
