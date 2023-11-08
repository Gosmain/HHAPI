import os

import telebot

from configs import config
from hh_api.hh_api import HeadHunterAPI
from hh_api.hh_data_process import HeadHunterDataProcessing as hhdp
from hh_api.hh_params import HeadHunterParametersForRequest
from hh_working_files.hh_inspector import HHInspector
from hh_working_files.hh_scribe import HHScribe

bot = telebot.TeleBot(os.environ['TOKEN'])


@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    """Метод для обработки сообщение в телеграм.

    :param message: сообщение от пользователя
    """

    lower_text = message.text.lower()

    if lower_text == "получить вакансии":

        with open('vacancies.txt', 'r') as f:

            for line in f.readlines():
                bot.send_message(message.from_user.id, line)

    elif lower_text == "обновить вакансии":

        HHScribe.clear_file('vacancies.txt')
        HHScribe.clear_file('req.txt')

        hh = HeadHunterAPI()

        for key in config.KEY_WORDS:

            params = HeadHunterParametersForRequest.vacancies(key, '1')
            # TODO все еще не тот тип, как в аннотации
            # TODO судя по всему номер страницы тебе надо передавать в этот билдер, подумай как лучше сделать,
            #  возможно генератор нужно будет написать)

            for element in hh.vacancies(params):

                string = f'{hhdp.get_name(element)} {hhdp.get_salary_value(element)} {hhdp.get_salary_currency(element)} {hhdp.get_link(element)}\n'

                if HHInspector.check_string('vacancies.txt', string):
                    # todo тут и простой функции было бы достаточно, название метода слабоватое, не понятно что за проверка строки
                    #  лучше что-то по смыслу подходящее, мб is_substring, is_subtext например
                    HHScribe.write_down('vacancies.txt', string)
                    HHScribe.write_down('req.txt', f'{hhdp.get_requirement(element)}\n')

        bot.send_message(message.from_user.id, "вакансии обновлены")

# TODO вижу у тебя в трех местах используется 'vacancies.txt'  и в двух 'req.txt' , переделай в константы
