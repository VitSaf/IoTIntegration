
from influxdb import InfluxDBClient, DataFrameClient
import pandas as pd


#подключение
client = InfluxDBClient(host = '192.168.88.177', port = 8086, username = , password  = )#username и password не забываем вводить
client.switch_database("iot")

#Пример данных: {'time': '2020-05-26T10:07:50.694000Z', 'gas1': 3.9519999027252197, 'gas2': 3.9733333587646484, 'gas3': 4.005333423614502, 'gas4': 0.0}
def get_gas_data():
	return client.query('SELECT "gas1", "gas2", "gas3", "gas4" FROM "gas"')
	#return client.query('SELECT *::field FROM "gas"')

#Пример данных: {'time': '2020-06-25T12:56:47.754000Z', 'temperature': 24.600000381469727}

def get_temperature_data(column_n):
	return client.query('SELECT "temperature" FROM "temperature" WHERE ("DevEUI" = ' + column_n)

def get_date_and_value(s):
	tmp = str(s).split(',')
	return tmp[0].split("'")[3], tmp[1].split()[1].split('}')[0]

#d, v = get_date_and_value("{'time': '2020-05-14T08:51:06.917000Z', 'current': 15.329999923706055}")
T112_1 = "'')"#дописать devEUI в ''
T112_2 = "'')"
T112_3 = "'fc0094000054b005')"
T112_4 = "'fc0094000054afcb')"
T112_5 = "'')"

col_n = ['', T112_1, T112_2, T112_3, T112_4, T112_5]

def get_112_n(n):
	RESULT = []
	for i in get_temperature_data(col_n[n]).get_points():
		d, v = get_date_and_value(str(i))
		RESULT.append({'Дата': d, 'Значение': v})
	pd.DataFrame(RESULT).to_excel('Выгрузка по 112-' + str(n) + '.xlsx')

get_112_n(3)
get_112_n(4)