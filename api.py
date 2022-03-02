import requests
import logging
import io

from abc import abstractmethod

HEADERS= {"User-Agent":'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) \
            AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.110 Safari/537.36'}
class Get:
    def __init__(self):
        self.headers = HEADERS

    def read(self, **params):
        resp = requests.get(self.url, headers=self.headers, params=params)
        return resp

    @property
    @abstractmethod
    def url(self):
        return NotImplementedError  #아직 구현하지 않은 부분

class Post:
    def __init__(self):
        self.headers = HEADERS

    def read(self, **params):
        resp = requests.post(self.url, headers=self.headers, data=params)
        return resp

    @property
    @abstractmethod
    def url(self):
        return NotImplementedError 
    
class KrxWebIo(Post):
    def read(self, **params):
        params.update(bld= self.bld)
        resp= super().read(**params)
        