"""Тут пишешь тесты."""
from decimal import Decimal
from hh_api.hh_api import HeadHunterAPI
from hh_api.hh_data_process import HeadHunterDataProcessing
from hh_api.hh_params import HeadHunterParametersForRequest
import pytest


@pytest.mark.parametrize("a, b, c, d", [("qa", 1, 1, True),
                                        ("aqa", -1, 3, False)])
def test_1(a, b, c, d):
  """Тест HeadHunterParametersForRequest.vacancies"""

  params = HeadHunterParametersForRequest.vacancies(text=a,
                                                    area=b,
                                                    per_page=c,
                                                    only_with_salary=d)
  assert params["text"] == f'NAME:{a}'
  assert params["area"] == b
  assert params["per_page"] == c
  assert params["only_with_salary"] is d


@pytest.mark.parametrize("salari_from, salary_to, salary_gross",
                         [(100_000, 500_000, True), (145_000, 350_000, True)])
def test_2(salari_from, salary_to, salary_gross):
  """Тест HeadHunterDataProcessing.get_salary_value. gross true"""

  salary = HeadHunterDataProcessing.get_salary_value({
      'salary': {
          'from': salari_from,
          'to': salary_to,
          'gross': salary_gross
      }
  })

  assert salary == Decimal((salari_from + salary_to) / 2 * 0.87)


@pytest.mark.parametrize("salari_from, salary_to, salary_gross",
                         [(100_000, 500_000, False),
                          (145_000, 350_000, False)])
def test_3(salari_from, salary_to, salary_gross):
  """Тест HeadHunterDataProcessing.get_salary_value. gross folse"""

  salary = HeadHunterDataProcessing.get_salary_value({
      'salary': {
          'from': salari_from,
          'to': salary_to,
          'gross': salary_gross
      }
  })

  assert salary == Decimal((salari_from + salary_to) / 2)


# пример теста
# пример запуска python -m pytest tests
