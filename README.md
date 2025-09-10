#### Build docker
```bash
docker-compose up -d --build 
```
#### Tạo topic kafka
```bash
docker exec -it kafka kafka-topics.sh --create --topic log_topic --bootstrap-server kafka:9092 --partitions 1 --replication-factor 1
```
#### Tạo log mẫu
```bash
docker exec -it flume python -u /opt/log/log_generator.py
```
### Chạy Spark Job:

#### Copy script Python vào container:
```bash
docker cp log_error_counter_structured.py spark-master:/opt/bitnami/spark/
```
#### Chạy:
```bash
docker exec spark-master /opt/bitnami/spark/bin/spark-submit --packages org.apache.spark:spark-sql-kafka-0-10_2.12:3.3.0 /opt/bitnami/spark/log_error_counter_structured.py
```

