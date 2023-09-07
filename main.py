from hh_api.hh_api import HeadHunterAPI as HeadHunterAPI
from hh_api.hh_params import HeadHunterParametersForRequest
from hh_api.hh_data_process import HeadHunterDataProcessing as hhdp
from configs import config

import telebot

bot = telebot.TeleBot(config.TOKEN)  # TODO уверен, что он должен быть глобальным?


@bot.message_handler(content_types=['text'])  # TODO давай вынесем в отдельную директорию tg_api/tg_bot/tg_handler
def get_text_messages(message):
    if message.text.lower() == "получить вакансии":
        with open('vacancies.txt', 'r') as f:
            for el in f.readlines():  # TODO переименуй эл на что-то понятное
                bot.send_message(message.from_user.id, el[:-2])
    elif message.text.lower() == "обновить вакансии":
        for key in config.KEY_WORDS:  # TODO избавляемся от кучи форов, подумай как проходить не вглубь, а вширь
            params = HeadHunterParametersForRequest.vacancies(
                key_words_in_vavancy_name=key,
                search_area=1,
                search_page=0,  # TODO надо сделать так, чтобы по всем страницам проходилось
                vacancy_per_page=100,
                vacancy_only_with_salary=True)
            data = hh.vacancies(params)
            for el in data['items']:  # TODO переименуй эл на что-то понятное
                if el not in final_data:
                    final_data.append(el)
        bot.send_message(message.from_user.id, "Вакансии обновлены")

        with open('req.txt', 'w',
                  encoding='utf-8') as r, open('vacancies.txt',
                                               'w',
                                               encoding='utf-8') as v:
            for el in final_data:  # TODO надо написать отдельную сущность, которая будет писать в файлы,
                # TODO на вход пусть будет набор параметров для записи и имя файла
                v.write(
                    f"{hhdp.get_link(el)} {hhdp.get_name(el)} {hhdp.get_salary_value(el)} {hhdp.get_salary_currency(el)}\n"
                )
                r.write(f"{hhdp.get_requirement(el)}\n")

    else:
        bot.send_message(message.from_user.id,
                         "Напишите 'получить вакансии' или 'обновить вакансии'")


if __name__ == '__main__':
    hh = HeadHunterAPI()

    final_data = []  # TODO зачем этот список объявлять тут?

    bot.polling(none_stop=True, interval=0)  # TODO а не надо передать hh в поллинг в качестве
    # todo какого-то параметра или чего-то подобного?
