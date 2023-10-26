from typing import Any, Dict


class HeadHunterParametersForRequest:
    '''Класс для формирования параметров для запроса к HeadHunterAPI.
    '''

    @staticmethod
    def vacancies(key_words_in_vavancy_name: str,
                  search_area: int,
                  vacancy_per_page: int = 100,
                  vacancy_only_with_salary: bool = True) -> Dict[str, Any]:
        '''Метод для формирования параметров для запроса к HeadHunterAPI.

        :param key_words_in_vavancy_name: ключевые слова в названии вакансии
        :param search_area: id района поиска
        :param vacancy_per_page: количество вакансий на страницу
        :param vacancy_only_with_salary: фильтр по вакансиям только с зарплатой
        :return: параметры для запроса к HeadHunterAPI
        '''
        return {
            'text': f"NAME:{key_words_in_vavancy_name}",
            'area': search_area,
            'per_page': vacancy_per_page,
            'only_with_salary': vacancy_only_with_salary
        }
