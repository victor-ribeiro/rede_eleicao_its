import twint as t
import pandas as pd
import json
from datetime import datetime
import time

class tweet_search(t.Config):
    def __init__(self, *args, **kwargs):
        super().__init__()
        for k,v in kwargs.items():
            self.__setattr__(k, v)
    def run(self):
        self.Store_csv= True
        self.Limit = 4000
        self.Retries_count = 5
        self.Output = 'data/%s-%s.csv' % (self.candidato, datetime.now().timestamp())
        t.run.Search(self)

if __name__ == "__main__":
    with open('config.json', 'r') as arq:
        data_file = arq.read()
        candidatos = json.loads(data_file,)
        for i in candidatos:
            candidato = tweet_search(**i)
            candidato.run()
        time.sleep(30*60)