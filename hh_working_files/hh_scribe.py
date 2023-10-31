class HHScribe:
    '''Класс для записи и удаления данных в файлы.
    '''

    @staticmethod
    def write_down(file_name, text):
        # TODO нет аннотации
        '''Метод для записи данных в файл.

        :param file_name: имя файла
        :param text: текст для записи
        '''
        with open(file_name, 'a', encoding='utf-8') as file:
            file.write(text)

    @staticmethod
    def clear_file(file_name):
        # TODO нет аннотации
        '''Метод для очистки файла.

        :param file_name: имя файла
        '''
        open(file_name, 'w')
