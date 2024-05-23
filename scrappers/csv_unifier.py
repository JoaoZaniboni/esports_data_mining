import pandas as pd

def unify_csv():
    df1 = pd.read_csv('../csvs/bo_data.csv', sep=';')
    df2 = pd.read_csv('../csvs/hltv_data.csv', sep=';')
    df3 = pd.read_csv('../csvs/liquipedia_data.csv', sep=';')


    # Juntar os dados usando a coluna 'Nome' como chave
    df_merged = pd.merge(df1, df2, on='Player', how='outer')
    df_merged = pd.merge(df_merged, df3, on='Player', how='outer')

    path = "../csvs/all_data.csv"
    df_merged.to_csv(path, index=False, sep=';')
    df_merged.to_html('../csvs/all_data.html', index=False)

if __name__ == '__main__':
    unify_csv()



