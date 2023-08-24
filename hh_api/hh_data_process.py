from typing import Any, Dict


class HeadHunterDataProcessing:

  @staticmethod
  def get_salary_value(item: Dict[str, Any]) -> str:
    if item['salary']['to'] and item['salary']['from']:
      return str((item['salary']['to'] + item['salary']['from']) / 2 * 0.87)
    elif item['salary']['to']:
      return str(item['salary']['to'] * 0.9 * 0.87)
    else:
      return str(item['salary']['from'] * 1.1 * 0.87)

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
