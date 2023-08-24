from hh_api.hh_api import HeadHunterAPI as HeadHunterAPI
from hh_api.hh_params import HeadHunterParametersForRequest
from hh_api.hh_data_process import HeadHunterDataProcessing as hhdp

key_words = ['python qa', 'python aqa', 'python автотестировщик']

if __name__ == '__main__':

  hh = HeadHunterAPI()

  for key in key_words:
    
    
    params = HeadHunterParametersForRequest.vacancies(key, 1, 0, 100, True)
    data = hh.vacancies(params)
    
      
    with open('req.txt', 'a', encoding='utf-8') as r, open('vacancies.txt', 'a', encoding='utf-8') as v:
      for el in data['items']:
        v.write(f"{hhdp.get_link(el)} {hhdp.get_name(el)} {hhdp.get_salary_value(el)} {hhdp.get_salary_currency(el)}\n")
        r.write(f"{hhdp.get_requirement(el)}\n")