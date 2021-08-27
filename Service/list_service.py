import requests
from requests.adapters import HTTPAdapter


class ListService(object):

    @staticmethod
    def find_list_page(page):
        session = requests.Session()
        session.mount("http://", HTTPAdapter(max_retries=3))

        url = f"http://challenge-api.luizalabs.com/api/product/?page={page}"
        response = session.get(url)
        result = response.json()
        return result

    @staticmethod
    def find_list_id(id):
        session = requests.Session()
        session.mount("http://", HTTPAdapter(max_retries=3))

        url = f"http://challenge-api.luizalabs.com/api/product/{id}/"
        response = session.get(url)
        result = response.json()
        return result
