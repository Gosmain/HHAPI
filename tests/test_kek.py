"""Тут пишешь тесты."""
from hh_api.hh_params import HeadHunterParametersForRequest


def test_1():
    """Первый тест."""

    params = HeadHunterParametersForRequest.vacancies(
        text="QA",
        area=1,
        per_page=1,
        only_with_salary=True
    )
    assert params["text"] == "NAME:QA"
    assert params["area"] == 1
    assert params["per_page"] == 1
    assert params["only_with_salary"] is True

# пример теста
# пример запуска python -m pytest tests