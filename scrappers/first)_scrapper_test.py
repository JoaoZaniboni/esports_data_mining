import requests
from bs4 import BeautifulSoup
import pandas as pd

url = 'https://liquipedia.net/counterstrike/Portal:Statistics/Player_earnings'

# Fazendo a solicitação HTTP
response = requests.get(url)

# Verifica se a solicitação foi bem-sucedida
if response.status_code == 200:
    # Parseando o conteúdo HTML
    soup = BeautifulSoup(response.text, 'html.parser')

    # Encontrando a primeira tabela na página
    tabela = soup.find('table')

    linhas = tabela.find_all('tr')
    first_line_columns = linhas[0].find_all("th")
    column_names = []
    for column in first_line_columns:
        name = column.get_text()
        if name == "":
            name = column.find("span").attrs["title"]
        column_names.append(name)

    dados = {column_name: [] for column_name in column_names}
    # removed_columns = ["#", "Achievements"]
    # for x in removed_columns:
    #     dados.pop(x)
    for linha in linhas:
        dados_linha = []
        colunas = linha.find_all('td')
        for column in colunas:
            dados_linha.append(column.get_text())

    df = pd.DataFrame(dados)
else:
    print("Falha ao carregar a página:", response.status_code)