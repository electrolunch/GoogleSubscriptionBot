import requests
from bs4 import BeautifulSoup

query = "python"
url = f"https://www.google.com/search?q={query}"
#%%
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36"
}
response = requests.get(url, headers=headers)
#%%
start_date = "08/01/2023"
end_date = "08/05/2023"
query = "tucan"
# Adding the date range filter to the URL
url = f"https://www.google.com/search?q={query}&tbs=cdr%3A1%2Ccd_min%3A{start_date}%2Ccd_max%3A{end_date}"

response = requests.get(url)
#%%
with open('response.html', 'w',encoding="utf-8") as f:
    f.write(response.text)

with open('response.html', 'r',encoding="utf-8") as f:
    html = f.read()

soup = BeautifulSoup(html, 'lxml')
# save to file
# soup.prettify()
results = soup.find('div', id='main') 

# Get all the result blocks 
blocks = results.find_all('div', class_='Gx5Zad')
block=blocks[7]
block.a['href']
# Extract data from each block
for block in blocks:
  title = block.h3.text
  link = block.a['href']
  snippet = block.find('div', class_='BNeawe').text
  
  print(title)
  print(link)
  print(snippet)