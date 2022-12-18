import os
import re
import time
from functions import unzip

def parser(file):
    tic = time.perf_counter()
    with open(file, "r") as file_for_parse:
        with open("results_files\\result_file_after_parse.csv", 'w') as result_file:
            while True:
                str = ""
                line = file_for_parse.readline()
                if not line:
                    break
                pattern = r'\w+\s+\d\s\d{2}:\d{2}:\d{2}\s(\w+\s(?:\w+\W)+)\s(\d+/\w+/\d+):(\d{2}:\d{2}:\d{2})\s(\W\d{' \
                          r'4})\s(\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3})\s-\s(\S+)\s(\S+)\s(\S+)\s(\S+)\s(\S+)\s(\S+)\s(' \
                          r'\S+)\s((?:\S+\s)+)'
                result = re.match(pattern, line).groups()
                for elem in result:
                    str = str + elem.strip() + ';'
                result_file.write(str + "\n")
    #удаляем файл, созданный после распаковки
    if os.path.isfile(file):
        os.remove(file)

    toc = time.perf_counter()
    print(f"Парсинг длился {toc - tic:0.4f} секунд")

if __name__ == '__main__':
    file = "csv_example.csv.gz"
    file_for_parse = unzip(file)
    parser(file_for_parse)

