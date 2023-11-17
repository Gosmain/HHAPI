"""Тут пишешь тесты."""
from decimal import Decimal
from hh_api.hh_api import HeadHunterAPI
from hh_api.hh_data_process import HeadHunterDataProcessing as hhdp
from hh_api.hh_params import HeadHunterParametersForRequest as hhpfr
import pytest


@pytest.mark.parametrize("text, area, per_page, only_with_salary", [("qa", 1, 1, True), ("aqa", -1, 3, False)])
def test_hhpfr_vacancies(text, area, per_page, only_with_salary):
    """Тест HeadHunterParametersForRequest.vacancies"""

    params = hhpfr.vacancies(text=text, area=area, per_page=per_page, only_with_salary=only_with_salary)
    assert params["text"] == f'NAME:{text}'
    assert params["area"] == area
    assert params["per_page"] == per_page
    assert params["only_with_salary"] is only_with_salary


@pytest.mark.parametrize("salari_from, salary_to, expexted_result",
                         [(100_000, 500_000, Decimal(261_000)),
                          (145_000, 350_000, Decimal(215_325))])
def test_hhdp_get_salary_value_gross_true(salari_from, salary_to,
                                          expexted_result):
    """Тест HeadHunterDataProcessing.get_salary_value. all True."""

    salary = hhdp.get_salary_value(
        {'salary': {
            'from': salari_from,
            'to': salary_to,
            'gross': True
        }})

    assert salary == expexted_result


@pytest.mark.parametrize("salari_from, salary_to, expexted_result",
                         [(100_000, 500_000, Decimal(300_000)),
                          (145_000, 350_000, Decimal(247_500))])
def test_hhdp_get_salary_value_gross_false(salari_from, salary_to,
                                           expexted_result):
    """Тест HeadHunterDataProcessing.get_salary_value. gross False. from, to - True."""

    salary = hhdp.get_salary_value(
        {'salary': {
            'from': salari_from,
            'to': salary_to,
            'gross': False
        }}
    )

    assert salary == expexted_result


@pytest.mark.parametrize("salary_to, expexted_result",
                         [(500_000, Decimal(391_500)),
                          (350_000, Decimal(274_050))])
def test_hhdp_get_salary_value_from_false(salary_to, expexted_result):
    """Тест HeadHunterDataProcessing.get_salary_value. gross, to - True. from - ''."""

    salary = hhdp.get_salary_value(
        {'salary': {
            'from': '',
            'to': salary_to,
            'gross': True
        }}
    )

    assert salary == expexted_result


@pytest.mark.parametrize("salary_from, expexted_result",
                         [(500_000, Decimal(478_500)),
                          (350_000, Decimal(334_950))])
def test_hhdp_get_salary_value_to_false(salary_from, expexted_result):
    """Тест HeadHunterDataProcessing.get_salary_value. gross, from - True. to - ''."""

    salary = hhdp.get_salary_value(
        {
            'salary':
                {
                    'from': salary_from,
                    'to': '',
                    'gross': True
                }
        }
    )

    assert salary == expexted_result


@pytest.mark.parametrize("salary_to, expexted_result",
                         [(500_000, Decimal(450_000)),
                          (350_000, Decimal(315_000))])
def test_hhdp_get_salary_value_from_false_gross_false(salary_to,
                                                      expexted_result):
    """Тест HeadHunterDataProcessing.get_salary_value. gross - False, to - True. from - ''."""

    salary = hhdp.get_salary_value(
        {'salary': {
            'from': '',
            'to': salary_to,
            'gross': False
        }}
    )

    assert salary == expexted_result


@pytest.mark.parametrize("salary_from, expexted_result",
                         [(500_000, Decimal(550_000)),
                          (350_000, Decimal(385_000))])
def test_hhdp_get_salary_value_to_false_gross_false(salary_from,
                                                    expexted_result):
    """Тест HeadHunterDataProcessing.get_salary_value. gross - False, from - True. to - ''."""

    salary = hhdp.get_salary_value(
        {'salary': {
            'from': salary_from,
            'to': '',
            'gross': False
        }})

    assert salary == expexted_result


@pytest.mark.parametrize("currency, expexted_result",
                         [("RUR", "RUR"), ("EUR", "EUR"), ("USD", "USD"),
                          ("", ""),
                          ("belarusskie_zaichiki", "belarusskie_zaichiki")])
def test_hhdp_get_salary_currency(currency, expexted_result):
    """Тест HeadHunterDataProcessing.get_salary_currency."""

    name_currency = hhdp.get_salary_currency({'salary': {'currency': currency}})

    assert name_currency == expexted_result


@pytest.mark.parametrize("link, expexted_result",
                         [("qa pithon", "qa pithon"),
                          ("aqa python", "aqa python"),
                          ("разработчик", "разработчик"), ("", "")])
def test_hhdp_get_link(link, expexted_result):
    """Тест HeadHunterDataProcessing.get_link."""

    vacanci_link = hhdp.get_link({'alternate_url': link})

    assert vacanci_link == expexted_result


@pytest.mark.parametrize("name, expexted_result",
                         [("qa pithon", "qa pithon"),
                          ("aqa python", "aqa python"),
                          ("разработчик", "разработчик"), ("", "")])
def test_hhdp_get_name(name, expexted_result):
    """Тест HeadHunterDataProcessing.get_name."""

    vacanci_name = hhdp.get_name({'name': name})

    assert vacanci_name == expexted_result


@pytest.mark.parametrize("requirement, expexted_result",
                         [("qa pithon", "qa pithon"),
                          ("aqa python", "aqa python"),
                          ("разработчик", "разработчик"), ("", "")])
def test_hhdp_get_requirement(requirement, expexted_result):
    """Тест HeadHunterDataProcessing.get_requirement."""

    vacanci_requirement = hhdp.get_requirement(
        {'snippet': {
            'requirement': requirement
        }})

    assert vacanci_requirement == expexted_result