build:
	docker build -t matthiasknight/udaconnect-location-api:latest .
clean:
	rm -rf venv/
push:
	docker push matthiasknight/udaconnect-location-api:latest
deploy:
	kubectl apply -f deployment/
undeploy:
	kubectl delete -f deployment/
