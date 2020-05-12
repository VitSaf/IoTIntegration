from concurrent import futures
import logging
import grpc
import iiot_device_pb2
import iiot_device_pb2_grpc


print("Before run")
def run():
    with grpc.insecure_channel('localhost:7654') as channel:
    	stub = iiot_device_pb2_grpc.IoTDeviceStub(channel)
    	response = stub.getDeviceList(iiot_device_pb2.DeviceListRequest())
    print("response: " + response.message)