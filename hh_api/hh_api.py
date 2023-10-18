from typing import Dict, Any, List

import requests


class HeadHunterAPI:

    def __init__(self):
        self.url = 'https://api.hh.ru/'
        self.result = []

    def vacancies(self, params: Dict[str, Any]) -> List[Any]:
      number_of_pages = requests.get(self.url + 'vacancies', params=params).json()['found']//100
      for i in range(0, number_of_pages+1):
        params['page'] = i
        result = requests.get(self.url + 'vacancies', params=params).json()
        self.result.extend(result['items'])
      return self.result
        
      

    
