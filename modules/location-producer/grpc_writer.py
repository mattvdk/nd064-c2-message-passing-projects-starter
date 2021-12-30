import grpc
from location_pb2 import LocationMessage
import location_pb2_grpc

print("Sending sample payload")

channel = grpc.insecure_channel("localhost:5005")
stub = location_pb2_grpc.LocationServiceStub(channel)

location = LocationMessage(
    person_id=1,
    longitude=37.556,
    latitude=-122.29,
)

response = stub.Create(location)