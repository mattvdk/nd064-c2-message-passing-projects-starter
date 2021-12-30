from concurrent import futures
from grpc import server as grpc_server
from json import dumps
from kafka import KafkaProducer
from location_pb2 import LocationMessage
from location_pb2_grpc import LocationService, add_LocationServiceServicer_to_server
from logging import getLogger, INFO, StreamHandler
from os import environ
from time import sleep

kafka_url = environ["KAFKA_URL"]
kafka_topic = environ["KAFKA_TOPIC"]

logger = getLogger(__name__)
logger.setLevel(INFO)
logger.addHandler(StreamHandler())

producer = KafkaProducer(bootstrap_servers=kafka_url)


class LocationServicer(LocationService):
    def Create(self, request, context):
        request_value = {
            "person_id": request.person_id,
            "longitude": request.longitude,
            "latitude": request.latitude,
        }
        logger.info(f"Receiving {request_value}")
        producer.send(kafka_topic, dumps(request_value).encode('utf-8'))
        return LocationMessage(**request_value)


server = grpc_server(futures.ThreadPoolExecutor(max_workers=2))
add_LocationServiceServicer_to_server(LocationServicer(), server)

logger.info("Server starting on port 5005...")
server.add_insecure_port("[::]:5005")
server.start()

try:
    while True:
        sleep(86400)
except KeyboardInterrupt:
    server.stop(0)