import pandas as pd
import json

candidatos = [
    "Renata Souza - PSOL", "Eduardo Paes - DEM",
    "Marcelo Crivela - PRB", "Benedita da Silva - PT",
    "Marta Rocha - PDT",
]

data = pd.read_excel('../Results_RJ_compilado.xlsx', sheet_name=candidatos)

perfis = []
for k, v in data.items():
    for perfil in v['Perfil Twitter']:
        tmp = {
            "Following": True,
            "Followers": True,
            "Likes": True,
            "Timestamp": True,
            "Tweet": True,
            "Mentions": True,
            "Retweet": True,
            "retweet_date": True
        }
        tmp.update(nome=perfil.replace('@', ''), Username=perfil.replace('@', ''))
        perfis.append(tmp)
with open('json/perfis.json', 'w') as arq:
    j = json.dumps(perfis, indent=True, )
    arq.writelines(j)
print(j)