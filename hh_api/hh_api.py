from typing import Dict, Any, List

import requests


class HeadHunterAPI:

    def __init__(self):
        self.url = 'https://api.hh.ru/'

    def vacancies(self, params: Dict[str, Any]) -> List[Any]:
        return requests.get(self.url + 'vacancies', params=params).json()
