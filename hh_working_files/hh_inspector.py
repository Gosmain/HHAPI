class HHInspector:
    '''Класс для проверки наличия строки в файле.
    '''

    @staticmethod
    def check_string(file_name, text):
        # TODO нет аннотации
        '''Метод для проверки наличия строки в файле.

        :param file_name: имя файла
        :param text: строка для проверки
        :return: результат проверки
        '''
        with open(file_name, 'r') as f:
            return text not in f.readlines()

# TODO я бы выделил простую функцию из этого и убрал бы в папку, например, utils
