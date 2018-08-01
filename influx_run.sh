#!/bin/sh

docker pull influxdb

docker run --rm -d --name influx -p 8086:8086 influxdb 
