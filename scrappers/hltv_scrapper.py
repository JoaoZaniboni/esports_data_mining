import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://www.hltv.org/stats/players?minMapCount=200'

# Making the HTTP request
response = requests.get(url)

# Checking if the request was successful
if response.status_code == 200:
    # Parsing the HTML content
    soup = BeautifulSoup(response.text, 'html.parser')

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

    removed_columns = ["#", "Achievements"]
    # for x in removed_columns:
    #     data.pop(x)
    lines = []
    for row in rows:
        row_data = []
        columns = row.find_all('td')
        for column in columns:
            row_data.append(column.get_text())
        lines.append(row_data)

    df = pd.DataFrame(data=lines, columns=column_names)
    df = df.drop(columns=removed_columns)
    df = df.dropna(subset=['Player'])
    path = "../csvs/liquipedia_data.csv"
    df.to_csv(path, index=False)
else:
    print("Failed to load the page:", response.status_code)