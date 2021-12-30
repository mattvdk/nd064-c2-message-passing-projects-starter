# Project Setup
## Install Kafka
`helm repo add bitnami ‌https://charts.bitnami.com/bitnami‌`
`helm repo update`
```
helm update --install kafka bitnami/kafka \
--set volumePermissions.enabled=true \
--set zookeeper.volumePermissions.enabled=true
```

### Validate correct Kafka installation with a test producer and consumer
`kubectl exec -it kafka-0 -- kafka-console-producer.sh --topic yourtopic --bootstrap-server kafka:9092`

`kubectl exec -it kafka-0 -- kafka-console-consumer.sh --bootstrap-server kafka:9092 --from-beginning --topic yourtopic`

## Deploy database and frontend app
`kubectl apply -f deployment/`

## Deploy location-api
`kubectl apply -f modules/location-api/deployment/`

## Deploy person-api
`kubectl apply -f modules/person-api/deployment/`

## Deploy location-consumer
`kubectl apply -f modules/location-consumer/deployment/`

## Deploy location-producer
`kubectl apply -f modules/location-producer/deployment/`
