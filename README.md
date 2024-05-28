# esports_data_mining
Portugues:
Trabalho final da matéria Tópicos Especiais em Gerência de Dados UFSC INE5454-05238/07208 (20241) Mineração de dados de esports, mais especificamente, de jogadores de Counter-Strike.

O trabalho está dividido em 3 códigos, cada um sendo um scraper dos sites escolhidos. Eles estão localizados dentro da pasta scraper, e os 3 sites escolhidos foram:

Liquipedia (https://liquipedia.net/counterstrike/Portal:Statistics/Player_earnings)<br>
HLTV (https://www.hltv.org/stats/players?minMapCount=200) <br>
BO3 (https://bo3.gg/players?period=all_time&tiers=s,a,b&games_count=30&tab=main&sort=rating&order=desc) <br>
Os dados extraídos foram então salvos em CSV, estando localizados na pasta csvs. Como todos os dados possuíam como chave primária o nome do jogador, todos os dados foram agrupados em um único CSV chamado all_data, também localizado nessa mesma pasta.

Para rodar os códigos de scraping, é necessário executar o comando pip install -r requirements.txt, o qual irá instalar as bibliotecas utilizadas.

------------------------------------------------------------------------------------------------------------------------------------------------------------

English:
Final project for the subject Special Topics in Data Management UFSC INE5454-05238/07208 (20241) Data Mining in esports, specifically Counter-Strike players.

The project is divided into 3 scripts, each one being a scraper for the chosen websites. They are located inside the scraper folder, and the 3 selected websites were:

Liquipedia (https://liquipedia.net/counterstrike/Portal:Statistics/Player_earnings) <br>
HLTV (https://www.hltv.org/stats/players?minMapCount=200) <br>
BO3 (https://bo3.gg/players?period=all_time&tiers=s,a,b&games_count=30&tab=main&sort=rating&order=desc) <br>
The extracted data was then saved in CSV files, which are located in the csvs folder. Since all the data used the player's name as the primary key, all the data was aggregated into a single CSV file called all_data, also located in the same folder.

To run the scraping scripts, it is necessary to execute the command pip install -r requirements.txt, which will install the required libraries.
