# Install Kafka
`helm repo add bitnami ‌https://charts.bitnami.com/bitnami‌`
`helm repo update`
```
helm update --install kafka bitnami/kafka \
--set volumePermissions.enabled=true \
--set zookeeper.volumePermissions.enabled=true
```
kubectl exec -it kafka-0 -- kafka-console-producer.sh --topic yourtopic --bootstrap-server kafka:9092

kubectl exec -it kafka-0 -- kafka-console-consumer.sh --bootstrap-server kafka:9092 --from-beginning --topic yourtopic