build:
	docker build -t matthiasknight/udaconnect-person-api:latest .
clean:
	rm -rf venv/
push:
	docker push matthiasknight/udaconnect-person-api:latest
deploy:
	kubectl apply -f deployment/
undeploy:
	kubectl delete -f deployment/
