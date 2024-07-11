import requests
import pandas as pd
pd.set_option("display.max_columns", 100)

#1. api_url = "https://fakestoreapi.com/docs"  for ecommerce datasets
#2. https://reqres.in/
#3. https://dummyapis.com/


response = requests.get("https://hub.dummyapis.com/employee?noofRecords=10&idStarts=1001", verify=False)

data = response.json()

df = pd.DataFrame(data=data)
print(df.head(5))