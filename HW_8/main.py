from File_manager.create_file_txt import create_file_txt
from File_manager.txt_to_json import txt_to_json
from File_manager.create_file_json import func
from File_manager.json_to_csv import json_to_csv
from File_manager.csv_to_json import csv_to_json
from File_manager.directory_reference import directory_reference

from pathlib import Path

if __name__ == '__main__':

    # создание файла с расширением txt с данными:  рандомное слово: рандомное значение
    create_file_txt('data.txt', 'w')
    for _ in range(10):
        create_file_txt('data.txt', 'a')

    # создание из файла txt нового файла json Имена пишите с большой буквы. Каждую пару сохраняйте с новой строки.
    txt_to_json('data.txt', 'data.json')

    # запись в json файл данных: имени, Id и уровня. Id -  ключ для имени. Все идентификаторы уникальны независимо от уровня доступа.
    func('data1.json')

    # перенос данных из json файла в файл csv
    json_to_csv('data1.json', 'data.csv')

    # запись из csv файла  в json файл, где каждая строка csv файла представлена как отдельный json словарь
    csv_to_json('data.csv', 'data2.json')

    # спрвавочник по содержимому директория: (наименование объекта, тип объекта в директории, размер объекта, родительский директорий объекта)
    directory_reference(Path(Path.cwd()))
