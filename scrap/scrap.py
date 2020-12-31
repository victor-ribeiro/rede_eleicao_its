import twint as t
import json
from datetime import datetime
import time

class tweet_search(t.Config):
    def __init__(self, *args, **kwargs):
        super().__init__()
        for k,v in kwargs.items():
            self.__setattr__(k, v)
    def run(self):
        self.Since = '2020-01-01'
        self.Store_csv= True
        self.Show_hashtags = True
        self.Profile_full = True
        self.Limit = 4000
        self.Retries_count = 5
        self.Output = 'scrap/data/%s-%s.csv' % (self.nome, datetime.now().timestamp())
        t.run.Search(self)

if __name__ == "__main__":
    with open('json/config.json', 'r') as arq:
        data_file = arq.read()
        candidatos = json.loads(data_file,)
        for i in candidatos:
            candidato = tweet_search(**i)
            candidato.run()
    print('esperando:', end='\n\n')
    time.sleep(5*60)