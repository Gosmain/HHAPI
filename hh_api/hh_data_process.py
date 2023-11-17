from decimal import Decimal, ROUND_FLOOR
from typing import Any, Dict

from configs import config


class HeadHunterDataProcessing:
    """Класс для обработки данных с hh.ru."""

    @staticmethod
    def get_salary_value(item: Dict[str, Any]) -> Decimal:
        """Метод для получения значение зарплаты из вакансии.

        :param item: вакансия
        :return: значение зарплаты
        """

        salary_gross = item['salary']['gross']
        salary_to = item['salary']['to']
        salary_from = item['salary']['from']
        tax = 0.87 if salary_gross is True else 1
        if salary_to and salary_from:
            num = Decimal((salary_to + salary_from) / 2 * tax)
        elif salary_to:
            num = Decimal(salary_to * config.REDUCING_FACTOR * tax)
        else:
            num = Decimal(salary_from * config.INCREACING_FACTOR * tax)
        return num.quantize(Decimal('1.00'), ROUND_FLOOR)

    @staticmethod
    def get_salary_currency(item: Dict[str, Any]) -> str:
        """Метод для получения значения валюты из вакансии.

        :param item: вакансия
        :return: значение валюты
        """
        return item['salary']['currency']

    @staticmethod
    def get_link(item: Dict[str, Any]) -> str:
        """Метод для получения ссылки на вакансию.

        :param item: вакансия
        :return: ссылка
        """
        return item['alternate_url']

    @staticmethod
    def get_name(item: Dict[str, Any]) -> str:
        """Метод для получения названия вакансии.

        :param item: вакансия
        :return: имя
        """
        return item['name']

    @staticmethod
    def get_requirement(item: Dict[str, Any]) -> str:
        """Метод для получения требований из вакансии.

        :param item: вакансия
        :return: требования
        """
        return item['snippet']['requirement']
