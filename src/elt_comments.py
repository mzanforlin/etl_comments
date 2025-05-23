import pandas as pd
from sqlalchemy import create_engine
import requests
import psycopg2
from dotenv import load_dotenv
import json
import os

load_dotenv()

DB_HOST = os.getenv('DB_HOST_PROD')
DB_PORT = os.getenv('DB_PORT_PROD')
DB_NAME = os.getenv('DB_NAME_PROD')
DB_USER = os.getenv('DB_USER_PROD')
DB_PASS = os.getenv('DB_PASS_PROD')
DB_SCHEMA = os.getenv('DB_SCHEMA_PROD')

DATABASE_URL = f"postgresql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}"

engine = create_engine(DATABASE_URL)

url = 'https://jsonplaceholder.typicode.com/posts'

def extrair_dados():

    resp = requests.get(url)

    if resp.status_code == 200:
        dados_json = resp.json()
        df = pd.DataFrame(dados_json)
        return df
    else:
       print(f'deu um erro aqui : {resp.status_code}')
       return None
    
def salvar_dados(df):
    salvar = df.to_sql('comentarios',engine,if_exists = 'replace', index = False, schema = 'dbo')
    print("Dados salvos com sucesso!")


# Execução principal
if __name__ == "__main__":
    df_extraido = extrair_dados()
    if df_extraido is not None:
        salvar_dados(df_extraido)