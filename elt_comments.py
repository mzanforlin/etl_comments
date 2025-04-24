import pandas as pd
from sqlalchemy import create_engine
import requests
import psycopg2
import json

url = 'https://jsonplaceholder.typicode.com/posts'

response_status = requests.get(url).status_code
response_json = requests.get(url)
resp = response_json.json()
df = pd.DataFrame(resp).json

display(df)