from selenium import webdriver
from selenium.webdriver import chrome
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
import pandas as pd

options = webdriver.ChromeOptions()
options.add_experimental_option("detach", True)


# define the website to scrape
website = 'https://www.adamchoi.co.uk/overs/detailed'
driver = webdriver.Chrome(options=options,service=Service(ChromeDriverManager().install()))
# open Google Chrome with chromedriver
driver.get(website)

# locate and click on a button
all_matches_button =  driver.find_element("xpath",'//label[@analytics-event="All matches"]')
all_matches_button.click()
 
matches = driver.find_elements(By.TAG_NAME,'tr')
# print(matches)

# storage data in lists
date = []
home_team = []
score = []
away_team = []

# looping through the matches list
for match in matches:
    # print(match.text)
    date.append(match.find_element("xpath", './td[1]').text)     #"//tr/td[1]"
    home_team.append(match.find_element("xpath", './td[2]').text)
    score.append(match.find_element("xpath", './td[3]').text)
    away_team.append(match.find_element("xpath", './td[4]').text)

# quit drive we opened at the beginning
driver.quit()  

# Create Dataframe in Pandas and export to CSV (Excel)
df = pd.DataFrame({'date': date, 'Home Team': home_team, 'Score' : score, 'Away Team': away_team})
df.to_csv('football.csv', index=False)
print(df)