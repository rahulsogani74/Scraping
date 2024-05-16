import requests
import pandas as pd

url = "http://universities.hipolabs.com/search?country=india"

data_list = []

res = requests.get(url)

# print(res.content)
data = res.json() 

for item in data:
    # print(item)
    name = item.get("name")
    state = item.get("state-province")
    links = item.get("web_pages", [])
    
    # print(name, state, link)
    for link in links:
        data_list.append({"Name": name, "State": state, "Link": link})

df = pd.DataFrame(data_list)
df.to_excel("IndiaUniversitiesList.xlsx", index=False)