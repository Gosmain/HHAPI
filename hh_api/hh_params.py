from typing import Any, Dict


class HeadHunterParametersForRequest:
    '''Класс для формирования параметров для запроса к HeadHunterAPI.
    '''

    @staticmethod
    def vacancies(text: str,
                  area: int,
                  per_page: int = 100,
                  only_with_salary: bool = True) -> Dict[str, Any]:
        '''Метод для формирования параметров для запроса к HeadHunterAPI.

        :param text: ключевые слова в названии вакансии
        :param area: id района поиска
        :param per_page: количество вакансий на страницу
        :param only_with_salary: фильтр по вакансиям только с зарплатой
        :return: параметры для запроса к HeadHunterAPI
        '''
        return {
            'text': f"NAME:{text}",
            'area': area,
            'per_page': per_page,
            'only_with_salary': only_with_salary
        }
