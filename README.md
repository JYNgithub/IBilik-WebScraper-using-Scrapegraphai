# 🕷️ IBilik Web Scraper Using Scrapegraph-ai
 Scrapegraph-ai is a LLM-based web scraping Python library, meaning that web scrapping is now made easier by providing prompts for what to be scraped, without requiring advanced web programming knowledge.\
 This project aims to develop a web scrapping program to extract data on available rooms for rent in Cyberjaya, Selangor from https://www.ibilik.my/.\
 All data scraped are legal, open to public and for personal educational purposes. 

<p align="center">
  <img src="https://github.com/JYNgithub/IBilik-WebScraper-using-Scrapegraphai/blob/main/assets/Process.jpg" style="width: 90%;">
</p>

<p align="center">
  <img src="https://github.com/JYNgithub/IBilik-WebScraper-using-Scrapegraphai/blob/main/assets/Flowchart.jpg" style="width: 90%;">
</p>

# Installation
It is highly recommended to install these libraries in a virtual environment to avoid conflict with other libraries.
```bash
pip install -r requirements.txt
```
Note that this program currently only works for version 1.8.0 of Scrapegraphai.\
If the program does not work, you may verify the version by using:
```bash
pip show <package_name>
```

# Setup
## API Key 
You have to enter your API Key from your choice of LLM model into the .env file.
```
OPENAI_APIKEY = "insert api key here"
```
## Number of Pages
This will determine the number of pages you wish to scrap.
```python
# Specify number of pages to be scrapped
number_of_pages = 5
```
## Number of Rooms
This will determine the number of rooms for each page you wish to scrap.
```python
# Specify number of items (rooms) to be scrapped in each page
number_of_rooms = 20
```
## URL
By default, the URL will direct to the pages of rooms in Cyberjaya, Selangor.\ 
If you wish to change the link, simply add "&page=" to the end of the link. The link copied should be directly after searching for results in the home page.\ 
For example, "https://www.ibilik.my/rooms/kuantan?location_search=303&location_search_name=Kuantan%2C%20Pahang".
```python
main_url = f'https://www.ibilik.my/rooms/cyberjaya?location_search=54&location_search_name=Cyberjaya%2C+Selangor&page='
```
## Prompts
The desired prompts are entered here.
```python
# Specify prompts on what to be scraped
url_prompt = ['Identify the rental price.',
              'Identify the room type.',
              'List all the accommodations.']
```
Note that if you change the prompts, you should remove the code at line 92 to prevent any errors, which is only for data cleaning purposes.
```python
df.columns = ['Rental Price','Room Type', 'Accommodation Facilities','Link']
```

# Example of Scraped Data
The 'example_scraped_data.csv' is a sample of the results from this web scraper. It contains data of 100 rooms for rent in Cyberjaya, Selangor as of 12 July 2024.

# Disclaimer
All data scraped are legal and open to public. No user info has been extracted or utilized. The data is only used for personal and educational purposes.


 
