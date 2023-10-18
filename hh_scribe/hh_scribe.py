class HHScribe():

  @staticmethod
  def write_down(file_name, text):
    with open (file_name, 'a', encoding='utf-8') as file, open (file_name, 'r', encoding='utf-8') as r:
      if text not in r.readlines():
        file.write(text)

  @staticmethod
  def clear_file(file_name):
    open(file_name, 'w')

  