import os   
import pandas as pd
import time
from dotenv import load_dotenv
from scrapegraphai.graphs import SmartScraperGraph, OmniScraperGraph
load_dotenv()

# Specify API key
openai_key = os.getenv("OPENAI_APIKEY") ### Paste your API key at .env file
graph_config = {
    "llm": {
        "api_key": openai_key,
        "model": "gpt-3.5-turbo", # Specify your choice of LLM model
        "temperature":0
    },
    "verbose":True
}

# Specify number of pages to be scrapped
number_of_pages = 5

# Specify number of items (rooms) to be scrapped in each page
number_of_rooms = 20

# Specify URL with pagination (By default, the link scrapes data from rooms available in Cyberjaya, Selangor.)
main_url = f'https://www.ibilik.my/rooms/cyberjaya?location_search=54&location_search_name=Cyberjaya%2C+Selangor&page='
src = [main_url + str(num) for num in range(1, number_of_pages + 1)]
src_prompt = 'List me the URL of all the rooms. Do not create an array.'

# Specify prompts on what to be scraped
url_prompt = ['Identify the rental price.',
              'Identify the room type.',
              'List all the accommodations.']

i = 0
df = pd.DataFrame() 
temp = pd.DataFrame()
for pages in src:
    i+=1
    omni_scraper = OmniScraperGraph(
        prompt = src_prompt,
        source = pages, 
        config = graph_config
    )
    result = omni_scraper.run()

    for key, value in result.items():
        if isinstance(value, dict):
            urls = list(value.values())
            break
    
    print(f"Obtained a total of {len(urls)} of URLs (rooms) from Page {i}.")
    for url in urls:
        print(url)
    print()
    
    j = 0
    for url in urls:
        j+=1
        print("***************************")
        print(f"Scraping Page {i} URL {j}")
        print("***************************\n")
        
        for prompts in url_prompt:
            scrape_page = SmartScraperGraph(
                prompt=prompts,
                source=url, 
                config=graph_config
            )
            result = scrape_page.run()
            print(result)
            print()
            scraped_data = pd.DataFrame([result])
            temp = pd.concat([temp, scraped_data], axis=1)
            
        scraped_url = pd.DataFrame([url], columns = ['URL'])
        temp = pd.concat([temp, scraped_url], axis=1)
            
        df = pd.concat([df,temp])
        temp = pd.DataFrame()
        
        # Set to pause for 10 seconds after every two items
        if j < number_of_rooms:
            if j % 2 ==0:
                print("Wait for 10 second request interval.")
                time.sleep(10)
        else: 
            break
        print()


df.columns = ['Rental Price','Room Type', 'Accommodation Facilities','Link']

# Explore data
print("-------------------------------------------")
print("Check for missing values:")
print(df.isnull().sum())
print("-------------------------------------------")
print(df.info())
print("-------------------------------------------")

# Export data
df.to_csv('scraped_data.csv', index = False)
print("\nData merged and saved to 'scraped_data.csv' successfully.")
            
        
        
    
    


