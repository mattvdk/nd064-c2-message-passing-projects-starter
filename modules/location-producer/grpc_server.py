from concurrent import futures
from location_pb2 import LocationMessage
import location_pb2_grpc
import grpc
from time import sleep


class LocationServicer(location_pb2_grpc.LocationService):
    def Create(self, request, context):
        request_value = {
            "person_id": request.person_id,
            "lng": request.lng,
            "lat": request.lat,
        }
        print(request_value)
        return LocationMessage(**request_value)

server = grpc.server(futures.ThreadPoolExecutor(max_workers=2))
location_pb2_grpc.add_LocationServiceServicer_to_server(LocationServicer(), server)

print("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

try:
    while True:
        sleep(86400)
except KeyboardInterrupt:
    server.stop(0)