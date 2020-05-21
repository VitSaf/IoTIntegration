from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc
import xlwt
import xlrd
#import PySimpleGUI as sg
from xlutils.copy import copy
from datetime import datetime
from google.protobuf.timestamp_pb2 import Timestamp

#install xlwt,xlrd,xlutils, protobuf3

#form = sg.FlexForm('Форма')

#layout = [[sg.Text('Введите eui датчика'), sg.InputText(), sg.Submit()]]
#window = sg.Window(layout)
#button, values = f

def proto(ts1, ts2, eui):
    msg = iiot_device_pb2.DeviceHistoryRequest()
    msg.from_ts.CopyFrom(ts1)
    msg.to_ts.CopyFrom(ts2)
    #deveui = msg.devEuiList.add()
    #deveui.devEuiList = eui
    msg.devEuiList.append(eui)
    return msg


def getChannel():
	return grpc.insecure_channel('127.0.0.1:7655')

def getDevices():
    with grpc.insecure_channel('127.0.0.1:7655') as channel:
    	stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
    	response = stub.getDeviceList(iiot_device_pb2.DeviceListRequest())
    print("Response: " + str(response))


def getHist():
    channel = getChannel()
    stub = iiot_device_pb2_grpc.IotDeviceStub(channel)
    ts1 = Timestamp()
    ts1.FromDatetime(datetime(2020, 4, 20, 0, 0))#Дата от(год, месяц, день, час, минута)
    ts2 = Timestamp()
    ts2.FromDatetime(datetime(2020, 5, 20, 1, 0))#Дата до(год, месяц, день, час, минута)
    deveui = '3135323976376f01' #eui датчика, есть https://127.0.0.1/sensor-list столбец DevEUI
    #response = stub.getDeviceHistory(from_ts = ts1, to_ts = ts2, )
    response = stub.getDeviceHistory(proto(ts1, ts2, deveui))
    #print("Response: " + str(response.body.sensors[0].history[0].value))
    return response



def newExcel():
    wb = xlwt.Workbook()
    ws = wb.add_sheet('Results')
    wb.save('res.xls')
    print('Created')

def toExcel(date, value):
    rb = xlrd.open_workbook('res.xls')
    r_sheet = rb.sheet_by_index(0)
    r = r_sheet.nrows
    wb = copy(rb)
    sheet = wb.get_sheet(0)
    sheet.write(r ,0 ,date)
    sheet.write(r, 1, value)
    wb.save('res.xls')
    print('added')

#ToDatetime
history = getHist().body.sensors[0].history
print(len(history))
newExcel()
for i in history:
    print(str(i))
    tmp = str(i.value).split()[1]
    toExcel(str(i.ts.ToDatetime()), str(tmp))
    #toExcel(i.ts.ToDatetime(), i.value)
#getDevices()


