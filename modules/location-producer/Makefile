build:
	docker build -t matthiasknight/udaconnect-location-producer:latest .
proto-convert:
	python -m grpc_tools.protoc -I./ --python_out=./ --grpc_python_out=./ location.proto
clean:
	rm -rf venv/
push:
	docker push matthiasknight/udaconnect-location-producer:latest
deploy:
	kubectl apply -f deployment/
undeploy:
	kubectl delete -f deployment/
