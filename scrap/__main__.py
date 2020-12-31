import json
import scrap
import time
import os


def read_json(arq):
    with open(arq, 'r') as config:
        tmp = config.read()
        return json.loads(tmp)

root = os.path.abspath(os.path.dirname(__file__))
json_path = os.path.join(root, 'json')
c_path = os.path.join(json_path, 'config.json')
p_path = os.path.join(json_path, 'perfis.json')
print(json_path)

candidatos = read_json(c_path)
perfis = read_json(p_path)
perfis.extend(candidatos)


for perfil in perfis:
    p = scrap.tweet_search(**perfil)
    print(p.nome)
    p.run()
    print('esperando:', end='\n\n')
    time.sleep(5*60)