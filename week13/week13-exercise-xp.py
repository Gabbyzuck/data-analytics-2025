# Exercise 1: Parsing HTML with BeautifulSoup

# from bs4 import BeautifulSoup

# html_doc = """
# <!DOCTYPE html>
# <html lang="en">
# <head>
#     <meta charset="UTF-8">
#     <meta name="viewport" content="width=device-width, initial-scale=1.0">
#     <title>Sports World</title>
#     <style>
#         body { font-family: Arial, sans-serif; }
#         header, nav, section, article, footer { margin: 20px; padding: 15px; }
#         nav { background-color: #333; }
#         nav a { color: white; padding: 14px 20px; text-decoration: none; display: inline-block; }
#         nav a:hover { background-color: #ddd; color: black; }
#         .video { text-align: center; margin: 20px 0; }
#     </style>
# </head>
# <body>

#     <header>
#         <h1>Welcome to Sports World</h1>
#         <p>Your one-stop destination for the latest sports news and videos.</p>
#     </header>

#     <nav>
#         <a href="#football">Football</a>
#         <a href="#basketball">Basketball</a>
#         <a href="#tennis">Tennis</a>
#     </nav>

#     <section id="football">
#         <h2>Football</h2>
#         <article>
#             <h3>Latest Football News</h3>
#             <p>Read about the latest football matches and player news.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/football-video-id" frameborder="0" allowfullscreen>
#                 </iframe>
#             </div>
#         </article>
#     </section>

#     <section id="basketball">
#         <h2>Basketball</h2>
#         <article>
#             <h3>NBA Highlights</h3>
#             <p>Watch highlights from the latest NBA games.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/basketball-video-id" frameborder="0" allowfullscreen>
#                 </iframe>
#             </div>
#         </article>
#     </section>

#     <section id="tennis">
#         <h2>Tennis</h2>
#         <article>
#             <h3>Grand Slam Updates</h3>
#             <p>Get the latest updates from the world of Grand Slam tennis.</p>
#             <div class="video">
#                 <iframe width="560" height="315" src="https://www.youtube.com/embed/tennis-video-id" frameborder="0" allowfullscreen></iframe>
#             </div>
#         </article>
#     </section>

#     <footer>
#         <form action="mailto:contact@sportsworld.com" method="post" enctype="text/plain">
#             <label for="name">Name:</label><br>
#             <input type="text" id="name" name="name"><br>
#             <label for="email">Email:</label><br>
#             <input type="email" id="email" name="email"><br>
#             <label for="message">Message:</label><br>
#             <textarea id="message" name="message" rows="4" cols="50"></textarea><br><br>
#             <input type="submit" value="Send">
#         </form>
#     </footer>

# </body>
# </html>
# """

# soup = BeautifulSoup(html_doc,'html.parser')

# print(soup.title.get_text())

# soup.find_all("p")
# for p in soup.find_all("p"):
#     print(p.get_text())

# links = soup.find_all("a")
# for link in links:
#     print(link.get("href"))


#Exercise 2 : Scraping robots.txt from Wikipedia

# import requests
# from bs4 import BeautifulSoup

# headers = {"User-Agent": "Gabby/1.0 (week 13 exercise)"}

# response = requests.get("https://en.wikipedia.org/robots.txt", headers=headers)

# response = requests.get("https://en.wikipedia.org/robots.txt", headers=headers)

# print(response.text)

#Exercise 3 : Extracting Headers from Wikipedia’s Main Page

# import requests
# from bs4 import BeautifulSoup

# headers = {"User-Agent": "Gabby/1.0 (week 13 exercise)"}

# url = "https://en.wikipedia.org/wiki/Web_scraping"
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# headers_tags = soup.find_all(["h1", "h2", "h3", "h4", "h5", "h6"])
# for tag in headers_tags:
#     print(f"{tag.name}: {tag.get_text(strip=True)}")

#Exercise 4 : Checking for Page Title

# import requests
# from bs4 import BeautifulSoup

# url = "https://en.wikipedia.org/wiki/Web_scraping"

# headers = {"User-Agent": "Gabby/1.0 (week 13 exercise)"}
# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# if soup.title:
#     print("The page has a title:", soup.title.get_text())
# else:
#     print("The page does NOT have a title.")

#Exercise 5 : Analyzing US-CERT Security Alerts

# import requests
# from bs4 import BeautifulSoup
# from datetime import datetime

# url = "https://www.cisa.gov/news-events/cybersecurity-advisories?f%5B0%5D=advisory_type%3A93"

# headers = {"User-Agent": "Gabby/1.0 (week 13 exercise)"}

# response = requests.get(url, headers=headers)
# soup = BeautifulSoup(response.text, "html.parser")

# current_year = str(datetime.now().year)

# alerts = soup.find_all("body", class_="path-node not-front node-page node-page--node-type-flexible-page")

# current_year_alerts = [alert for alert in alerts if current_year in alert.get_text()]

# print(f"Number of US-CERT alerts in {current_year}: {len(current_year_alerts)}")

#Exercise 6 : Scraping Movie Details

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random

service = Service("/usr/local/bin/chromedriver")
driver = webdriver.Chrome(service=service)

url = "https://www.imdb.com/list/ls091294718/"
driver.get(url)

movies = WebDriverWait(driver, 10).until(
    EC.presence_of_all_elements_located((By.CSS_SELECTOR, "div.lister-item-content > h3.lister-item-header"))
)

random.shuffle(movies)
top_10 = movies[:10]

for movie in top_10:
    name = movie.find_element(By.TAG_NAME, "a").text
    year_tag = movie.find_element(By.CLASS_NAME, "lister-item-year")
    year = year_tag.text.strip("()") if year_tag else "N/A"
    
    parent = movie.find_element(By.XPATH, "./ancestor::div[contains(@class,'lister-item-content')]")
    summary_tag = parent.find_elements(By.CSS_SELECTOR, "p.text-muted")
    summary = summary_tag[1].text if len(summary_tag) > 1 else "No summary available"
    
    print(f"Name: {name}\nYear: {year}\nSummary: {summary}\n{'-'*50}")

driver.quit()