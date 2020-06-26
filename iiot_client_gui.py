import tkinter as tk
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import iiot_client as cli
import influxDBMngr as db
#нет datetime пикера
#Вводим строкой и парсим в datetime (есть готовая функция кажись)

#https://younglinux.info/tkinter/tkinter.php

def prepare_start(event):
	tmp_date = datetime.strptime(from_ts.get(), '%Y-%m-%d %H:%M')
	print(str(tmp_date))
	ts1 = Timestamp()
	ts1.FromDatetime(tmp_date)
	print(str(ts1))
	tmp_date1 = datetime.strptime(to_ts.get(), '%Y-%m-%d %H:%M')
	print(str(tmp_date1))
	ts2 = Timestamp()
	ts2.FromDatetime(tmp_date1)
	print(str(ts2))
	deveui = eui.get()
	print("cli.start")
	cli.start(ts1, ts2, deveui)

def get_t(event):
	db.start_t()

root = tk.Tk()
dates_frame = tk.Frame(root)
eui_label = tk.Label(root, text = 'Введите eui')
eui = tk.Entry(root, width = 25) #TODO в каком формате дату?
ts_label = tk.Label(root, text = 'Введите за какой промежуток делать выгрузку(даты в формате YYYY-MM-DD HH:MM)')
from_ts = tk.Entry(dates_frame, width = 15)
to_ts = tk.Entry(dates_frame, width = 15)
btn = tk.Button(root, text = 'Выгрузить')#btn вызывает cli.start(ts1, ts2, deveui)
#gas_btn = tk.Button(root, text = 'Выгрузить данные от газоанализаторов(influxDB)')
t_btn   = tk.Button(root, text = 'Выгрузить данные по температуре изinfluxDB')
#string to datetime 
#https://stackabuse.com/converting-strings-to-datetime-in-python/
btn.bind('<Button-1>', prepare_start)
t_btn.bind('<Button-1', get_t)

eui_label.pack()
eui.pack()
ts_label.pack()
dates_frame.pack()
from_ts.pack(side = tk.LEFT)
to_ts.pack(side = tk.RIGHT)
btn.pack()
t_btn.pack()
root.mainloop()
