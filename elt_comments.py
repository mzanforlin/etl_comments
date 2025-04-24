import pandas as pd
from sqlalchemy import create_engine
import requests
import psycopg2
import json

url = 'https://jsonplaceholder.typicode.com/posts'

response = requests.get(url)
resp = response.json()

print(resp)