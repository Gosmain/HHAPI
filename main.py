from hh_api.hh_api import HeadHunterAPI as HeadHunterAPI
from hh_api.hh_params import HeadHunterParametersForRequest
from hh_api.hh_data_process import HeadHunterDataProcessing as hhdp
from configs import config

import telebot

bot = telebot.TeleBot(config.TOKEN)


@bot.message_handler(content_types=['text'])
def get_text_messages(message):

  if message.text.lower() == "получить вакансии":
    with open('vacancies.txt', 'r') as f:
      for el in f.readlines():
        bot.send_message(message.from_user.id, el[:-2])
  elif message.text.lower() == "обновить вакансии":
    for key in config.KEY_WORDS:
      params = HeadHunterParametersForRequest.vacancies(key, 1, 0, 100, True)
      data = hh.vacancies(params)
      for el in data['items']:
        if el not in final_data:
          final_data.append(el)
    bot.send_message(message.from_user.id, "Вакансии обновлены")

    with open('req.txt', 'w',
              encoding='utf-8') as r, open('vacancies.txt',
                                           'w',
                                           encoding='utf-8') as v:
      for el in final_data:
        v.write(
          f"{hhdp.get_link(el)} {hhdp.get_name(el)} {hhdp.get_salary_value(el)} {hhdp.get_salary_currency(el)}\n"
        )
        r.write(f"{hhdp.get_requirement(el)}\n")

  else:
    bot.send_message(message.from_user.id,
                     "Напишите 'получить вакансии' или 'обновить вакансии'")


if __name__ == '__main__':

  hh = HeadHunterAPI()

  final_data = []

  bot.polling(none_stop=True, interval=0)
