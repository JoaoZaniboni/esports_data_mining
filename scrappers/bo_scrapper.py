from bs4 import BeautifulSoup
import pandas as pd
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
import time
driver = webdriver.Chrome()

url = 'https://bo3.gg/players?period=all_time&tiers=s,a,b&games_count=30&tab=main&sort=rating&order=desc'
# Abre a página no navegador
driver.get(url)
driver.maximize_window()
time.sleep(4)
action = ActionChains(driver)
action.move_by_offset(100, 100)
action.click()
action.perform()
while True:

    time.sleep(2)
    try:
        loading_element = driver.find_element(By.CLASS_NAME,'c-infinite-load-box')
        driver.execute_script("arguments[0].scrollIntoView();", loading_element)
    except Exception:
        break
    time.sleep(2)

html = driver.page_source
driver.quit()

soup = BeautifulSoup(html, 'html.parser')

columns = soup.find("div", class_="table-row").find_all("div", class_="table-cell")
columns_names = [x.get_text() for x in columns]
# removed_columns = []
# for x in removed_columns:
#     data.pop(x)
rows = soup.find("div", class_="table-group").find_all("a", class_="table-row")
all_rows_data = []
for row in rows:
    row_data = []
    columns = row.find_all("div", class_="table-cell")
    for column in columns:
        player = column.find("div", class_="player-info")
        if player:
            row_data.append(player.get_text())
        else:
            row_data.append(column.get_text())
    all_rows_data.append(row_data)
df = pd.DataFrame(data=all_rows_data, columns=columns_names)
# df = df.drop(columns=removed_columns)
df = df.dropna(subset=['Player'])
df = df.drop(df.columns[0], axis=1)
path = "../csvs/bo_data.csv"
df.to_csv(path, index=False, sep=';')
