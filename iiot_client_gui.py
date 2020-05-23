import tkinter as tk
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp
import iiot_client as cli
#нет datetime пикера
#Вводим строкой и парсим в datetime (есть готовая функция кажись)

#https://younglinux.info/tkinter/tkinter.php

def prepare_start(event):
	tmp_date = datetime.strptime(from_ts.get(), '%Y-%m-%d %H:%M')
	ts1 = Timestamp()
	ts1.FromDatetime(tmp_date)
	tmp_date = datetime.strptime(to_ts.get(), '%Y-%m-%d %H:%M')
	ts2 = Timestamp()
	ts2.FromDatetime(tmp_date)
	deveui = eui.get()
	print("cli.start")
	cli.start(ts1, ts2, deveui)

root = tk.Tk()
dates_frame = tk.Frame(root)
eui_label = tk.Label(root, text = 'Введите eui')
eui = tk.Entry(root, width = 25) #TODO в каком формате дату?
ts_label = tk.Label(root, text = 'Введите за какой промежуток делать выгрузку(даты в формате YYYY-MM-DD HH:MM)')
from_ts = tk.Entry(dates_frame, width = 15)
to_ts = tk.Entry(dates_frame, width = 15)
btn = tk.Button(root, text = 'Выгрузить')#btn вызывает cli.start(ts1, ts2, deveui)
#string to datetime 
#https://stackabuse.com/converting-strings-to-datetime-in-python/
btn.bind('<Button-1>', prepare_start)

eui_label.pack()
eui.pack()
ts_label.pack()
dates_frame.pack()
from_ts.pack(side = tk.LEFT)
to_ts.pack(side = tk.RIGHT)
btn.pack()
root.mainloop()