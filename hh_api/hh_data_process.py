from typing import Any, Dict
from configs import config
from decimal import Decimal, ROUND_FLOOR


class HeadHunterDataProcessing:

  

  @staticmethod
  def get_salary_value(item: Dict[str, Any]) -> str:
    tax = 0.87 if item['salary']['gross'] == True else 1
    if item['salary']['to'] and item['salary']['from']:
      num = Decimal((item['salary']['to'] + item['salary']['from']) / 2 * tax)
    elif item['salary']['to']:
      num = Decimal(item['salary']['to'] * config.REDUCING_FACTOR * tax)
    else:
      num = Decimal(item['salary']['from'] * config.INCREACING_FACTOR * tax)
    return num.quantize(Decimal('1.00'), ROUND_FLOOR)  

  @staticmethod
  def get_salary_currency(item: Dict[str, Any]) -> str:
    return item['salary']['currency']

  @staticmethod
  def get_link(item: Dict[str, Any]) -> str:
    return item['alternate_url']

  @staticmethod
  def get_name(item: Dict[str, Any]) -> str:
    return item['name']

  @staticmethod
  def get_requirement(item: Dict[str, Any]) -> str:
    return item['snippet']['requirement']
