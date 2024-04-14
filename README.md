# Mech-Index

First I learned how to make a web scraper. Then I used it to scrape Battlemechs from the [MUL Online Database](http://www.masterunitlist.info/Unit/Filter). Then I populated my own local sqlite db with the information, and created an app to access it via FastAPI.

There is no express purpose for this app, it is simply learning FastAPI and BeautifulSoup, but it may be interesting for anyone doing similar.

## Scraping

This section has a few different variations of BeautifulSoup to accomplish different scraping tasks:

### Text Scraper

This scrapes a table from a website url, and then writes the details to a file

### CSV Scraper (csvscraper.py)

This was my first scraper, made to capture a table and all its details regarding the mechs listed in the Master Unit List. After scraping the data, it's passed into a Pandas dataframe and further massaged by removing all the unnecessary columns before being saved as a csv file for import into sqlite

### Image Scraper (imagescraper.py)

This scraper goes through each page in a wiki category and finds every link associated with a mech. In this instance, there were 8 'next' pages, and a total of 1400+ mech pages to scrape. Once completed, it writes a file with a link to every url in the wiki category.

### mechfile.txt

This is the output of Image Scraper

### DL Image (dlimage.py)

This scraper opens a text list of urls and automatically downloads the original image associated with each one. This scrape will work on any Wiki style website, but you need to generate the text list first

### Images

This scraper combines the Image Scraper and DL Image functions into a single source, and keeps the list in memory rather than writing it to a file as an intermediate step

### Folder Scraper (folderscraper.py)

This scraper scans a designated folder (set in the path variable), and writes all the image names into a csv file. This can then be imported into SQL

## MechViewer

This section is the FastAPI build of a subset of the mechs that were scraped. Specifically, I grabbed all of the 'Mech Warrior Online' battlemechs, and made a smaller, more manageable database. Progress is ongoing, but the end result will be a full online viewer.

To see this in use, go to the 'Mech-Index' repo, or at this url:
