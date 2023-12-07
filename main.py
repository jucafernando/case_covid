import pandas as pd
import pyarrow
import gcsfs
import io
from datetime import datetime, date
from google.cloud import storage
from google.cloud import bigquery
import time

def rename_columns(df_teste):
     df_teste = df_teste.rename(columns={
          'date' : 'dt',
          'state': 'st',
          'city': 'city_column',
          'place_type': 'place_type',
          'confirmed': 'confirmed_cases',
          'deaths': 'deaths',
          'order_for_place' : 'order_place',
          'is_last' : 'is_last',
          'estimated_population_2019' : 'estimat_popul_2019',
          'estimated_population' : 'estimative_popilation',
          'city_ibge_code' : 'city_ibge_code',
          'confirmed_per_100k_inhabitants' : 'conf_100k_inhabits',
          'death_rate' : 'death_rate'})
     return df_teste

def case_covid(event, context):
     bucket_name = 'upload_covid_data_ex'
     file_path = event['name']
     fs = gcsfs.GCSFileSystem(project='tenacious-crane-406818')
     table_id = 'tenacious-crane-406818.covid.caso'
     projeto_id = 'tenacious-crane-406818'
     with fs.open(f'{bucket_name}/{file_path}', 'rb') as file:
          df_teste = pd.read_csv(file, sep=";")
          df_teste = rename_columns(df_teste)
          df_teste.to_gbq(table_id,project_id=projeto_id, if_exists='replace')
          
