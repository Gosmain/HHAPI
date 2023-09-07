from typing import Any, Dict


class HeadHunterParametersForRequest:

    @staticmethod
    def vacancies(
            key_words_in_vavancy_name: str,
            search_area: int,
            search_page: int = 0,
            vacancy_per_page: int = 20,
            vacancy_only_with_salary: bool = False
    ) -> Dict[str, Any]:
        return {
            'text': f"NAME:{key_words_in_vavancy_name}",
            'area': search_area,
            'page': search_page,
            'per_page': vacancy_per_page,
            'only_with_salary': vacancy_only_with_salary
        }
