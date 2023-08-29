from hh_api.hh_api import HeadHunterAPI as HeadHunterAPI
from hh_api.hh_params import HeadHunterParametersForRequest
from hh_api.hh_data_process import HeadHunterDataProcessing as hhdp

import telebot

bot = telebot.TeleBot('6687750926:AAGmMD08LR1bjZEtLiJR6SjoLOPzXEFMXYo')

key_words = ['python qa', 'python aqa', 'python автотестировщик']

if __name__ == '__main__':

  hh = HeadHunterAPI()

  final_data = []

  for key in key_words:    
    
    params = HeadHunterParametersForRequest.vacancies(key, 1, 0, 100, True)
    data = hh.vacancies(params)    
    for el in data['items']:
      if el not in final_data:
        final_data.append(el)
      
  with open('req.txt', 'a', encoding='utf-8') as r, open('vacancies.txt', 'a', encoding='utf-8') as v:
    for el in final_data:
      v.write(f"{hhdp.get_link(el)} {hhdp.get_name(el)} {hhdp.get_salary_value(el)} {hhdp.get_salary_currency(el)}\n")
      r.write(f"{hhdp.get_requirement(el)}\n")

  bot = telebot.TeleBot('6687750926:AAGmMD08LR1bjZEtLiJR6SjoLOPzXEFMXYo')

  @bot.message_handler(content_types=['text'])
  def get_text_messages(message):
    if message.text == "Поехали":
      with open('vacancies.txt', 'r') as f:
       for el in f.readlines():
         bot.send_message(message.from_user.id, el[:-2])
      

  bot.polling(none_stop=True, interval=0)

