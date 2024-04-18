import requests
from bs4 import BeautifulSoup
import pandas as pd

from selenium import webdriver

# Instancia um navegador (nesse caso, o Chrome)
driver = webdriver.Chrome()

# URL da página que você quer acessar
url = 'https://www.hltv.org/stats/players?minMapCount=200'

# Abre a página no navegador
driver.get(url)
# Obtém o HTML da página
html = driver.page_source
# Fecha o navegador
driver.quit()
soup = BeautifulSoup(html, 'html.parser')

# Finding the first table on the page
table = soup.find('table',  class_ = 'stats-table player-ratings-table')

rows = table.find_all('tr')
first_row_columns = rows[0].find_all("th")
column_names = []
for column in first_row_columns:
    name = column.get_text()
    if name == "":
        name = column.find("span").attrs["title"]
    column_names.append(name)

# removed_columns = []
# for x in removed_columns:
#     data.pop(x)
lines = []
for row in rows:
    row_data = []
    columns = row.find_all('td')
    for column in columns:
        if "teamCol" in column.attrs["class"]: #os times estao como imagens, entao pegar o nome das imagens
            imagens = column.find_all("a")
            teams = [x.attrs["href"].split("/")[-1] for x in imagens]
            row_data.append(teams)
        else:
            row_data.append(column.get_text())
    lines.append(row_data)
#<td class="teamCol" data-sort="Vitality" style="padding-top: 0px; padding-bottom: 0px;">
df = pd.DataFrame(data=lines, columns=column_names)
# df = df.drop(columns=removed_columns)
df = df.dropna(subset=['Player'])
path = "../csvs/hltv_data.csv"
df.to_csv(path, index=False, sep=';')
