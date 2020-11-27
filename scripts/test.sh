#! /bin/bash

cd service_1/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report term-missing

cd .. 

cd service_2/
pip3 install -r requirements.txt
python3 -m pytest --cov . --cov-report term-missing

cd ..
