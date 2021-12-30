build:
	docker build -t matthiasknight/udaconnect-location-consumer:latest .
clean:
	rm -rf venv/
push:
	docker push matthiasknight/udaconnect-location-consumer:latest
deploy:
	kubectl apply -f deployment/
undeploy:
	kubectl delete -f deployment/