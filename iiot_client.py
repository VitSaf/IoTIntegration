from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc


print("I'm working here!")
def run():
    with grpc.insecure_channel('localhost:8080') as channel:
    	stub = iiot_device_pb2_grpc.IoTDeviceStub(channel)
    	response = stub.getDeviceList(iiot_device_pb2.DeviceListRequest(token=''))
    print("It works! " + response.message)