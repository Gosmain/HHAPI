class HHScribe():  # TODO либо убери скобки, либо унаследуй класс от какого-то другого

    @staticmethod
    def write_down(file_name, text):
        with open(file_name, 'a', encoding='utf-8') as file, open(file_name, 'r',
                                                                  encoding='utf-8') as r:
            # TODO чет не понял зачем ты два раза читаешь один файл, прочитай про модификаторы доступа - a, r, wr
            #  https://pythonru.com/osnovy/fajly-v-python-vvod-vyvod
            if text not in r.readlines():
                # TODO если эта проверка нужна чтобы срезать повтораяющиеся вакансии, то я бы убрал из этого инструмента
                #  помним про уровни абстракции, этим должен заниматься кто-то другой, эта штука должна писать в файл
                file.write(text)

    @staticmethod
    def clear_file(file_name):
        open(file_name, 'w')
