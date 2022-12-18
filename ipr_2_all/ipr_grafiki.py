import functions
import pandas as pd


file = "u05smevosb02_srv01_access.log.gz_csv.gz"
file_for_df = functions.unzip(file)

#1. График интенсивности всех запросов

data_file = pd.read_csv(file_for_df, sep=";",
                        names=["host_ip", "date", "HTTP_Methods", "request", "HTTP_Version", "code_response", "id"])

data_file_06 = data_file[(data_file['date'] > '2015-02-06 00:00:00') & (data_file['date'] < '2015-02-06 23:59:00')].groupby('date').count()
functions.plotter("Интенсивность всех запросов", data_file_06)

#2. Графики интенсивности по отдельным запросам "/gateway/services/SID0003572/1.00", "/gateway/services/SID0003418/1.00" и т.д.

data_file_06 = data_file[(data_file['date'] > '2015-02-06 00:00:00') & (data_file['date'] < '2015-02-06 23:59:00')]

list_of_request = data_file_06['request'].value_counts().loc[lambda x : x > 1].to_frame()

for request_from_list in list_of_request.index.to_list():
    data_file_06 = data_file[(data_file['date'] > '2015-02-06 00:00:00') & (data_file['date'] < '2015-02-06 23:59:00')]
    data_file_06 = data_file_06[(data_file_06.request == request_from_list)].groupby('date').count()

    functions.plotter("Интенсивность запроса " + str(request_from_list)[18:28], data_file_06)

# 3. График интенсивности успешных и неуспешных запросов (200 и 500 ответ сервера)

code_response = [200, 500]
for code in code_response:
    data_file_06 = data_file[(data_file['date'] > '2015-02-06 00:00:00') & (data_file['date'] < '2015-02-06 23:59:00')]
    data_file_06 = data_file_06[(data_file_06.code_response == code)].groupby('date').count()
    functions.plotter("Интенсивность ответов с кодом " + str(code), data_file_06)

print("графики построены")