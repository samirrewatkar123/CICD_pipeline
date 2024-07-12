import requests
import pandas as pd
pd.set_option("display.max_columns", 100)

#1. api_url = "https://fakestoreapi.com/docs"  for ecommerce datasets
#2. https://reqres.in/
#3. https://dummyapis.com/

api = "https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001"

def read_api(url: str = api) ->pd.DataFrame:
    response = requests.get(url, verify=False)
    data = response.json()
    return pd.DataFrame(data=data)