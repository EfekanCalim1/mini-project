#! /bin/bash

docker build -t testing-image -f testing/Dockerfile .
docker run -it -d --name testing-container testing-image

docker exec testing-container pytest ./service_1 --cov ./service_1

docker exec testing-container pytest ./service_2 --cov ./service_2

docker stop testing-container
docker rm testing-container 
