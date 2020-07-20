
from influxdb import InfluxDBClient
import pandas as pd

HOST = '127.0.0.1'
PORT = 8086
USERNAME = ''
PASSWORD = ''


#подключение
client = InfluxDBClient(host = HOST, port = PORT, username = USERNAME, password  = PASSWORD)
client.switch_database("iot")

#Пример данных: {'time': '2020-05-26T10:07:50.694000Z', 'gas1': 3.9519999027252197, 'gas2': 3.9733333587646484, 'gas3': 4.005333423614502, 'gas4': 0.0}
def get_gas_data():
	return client.query('SELECT "gas1", "gas2", "gas3", "gas4" FROM "gas"')
	#return client.query('SELECT *::field FROM "gas"')

#Пример данных: {'time': '2020-06-25T12:56:47.754000Z', 'temperature': 24.600000381469727}
def get_temperature_data():
	return client.query('SELECT "temperature" FROM "temperature"')

#Пример данных: {'time': '2020-05-14T08:51:06.917000Z', 'current': 15.329999923706055}
def get_current_data():
	return client.query('SELECT "current" FROM "current"')

#Пример str: {'time': '2020-05-14T08:51:06.917000Z', 'current': 15.329999923706055}
#Возвращает дату(String) и значение(String)
def get_date_and_value(s):
	tmp = str(s).split(',')
	return tmp[0].split("'")[3], tmp[1].split()[1].split('}')[0]

#d, v = get_date_and_value("{'time': '2020-05-14T08:51:06.917000Z', 'current': 15.329999923706055}")
#print(d, v)

def start_t():
	RESULT = []
	for i in get_temperature_data().get_points():
		d, v = get_date_and_value(str(i))
		if float(v)*100%1 != 0 :
			RESULT.append({'Дата': d, 'Значение': v})
	pd.DataFrame(RESULT).to_excel('Выгрузка.xlsx')

start_t()


#print(str(client.get_list_database()))
#print(client.get_list_measurements())

#gas_data = get_gas_data()
#t_data = get_temperature_data()
#Что такое куррент?
#cur_data = get_current_data()

#p = gas_data.get_points()
#row = 0
#for i in p:
#	print(i, row)
#	row += 1