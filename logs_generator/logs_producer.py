import pandas as pd 
from kafka import KafkaConsumer
import os
from os import listdir
from os.path import isfile, join

class LogsProducer():
    def __init__(self,
                kafka_topic,
                kafka_bootstrap_servers=None,
                logs_path=None,
                structured_logs=True,
                component_number=5,
                lines_by_components=2000):
        self.kafka_topic = kafka_topic
        self.kafka_bootstrap_servers = os.getenv("LOGS_GENERATOR_kafka_bootstrap_servers")
        self.logs_path = os.getenv("LOGS_path")
        self.structured_logs = structured_logs
        self.component_number = component_number
        self.lines_by_components = lines_by_components
        self.kafka_producer = None
        # tuple to define a specific log file (Syslog/Syslog.log_structured.csv)
        self.specific_file = None

    def create_kafka_producer(self):
        self.kafka_producer = KafkaProducer(value_serializer=lambda v: json.dumps(v).encode('utf-8'))

    def read_logs(self):
        if specific_file != None:
            return [join(logs_path, self.specific_file)]
            
        logs_folder = [f for f in listdir(self.logs_path) if "." not in f]
        random_components = random.sample(logs_folders, self.component_number)
        logs_paths = []
        for component in random_components:s
            log_folder = join(logs_path, component)
            if self.structured_logs:
                component_logs_file = [f for f in listdir(join(logs_path, component)) if "structured.csv" in f][0]
                print(f"Structued logs file for component {component} are : {component_logs_file} \n")
                logs_paths.append(join(log_folder, component_logs_file))
        return logs_paths

    def produce_logs(self):
        _logs_paths = self.read_logs()
        for _log_file in _logs_paths:
            component_logs = pd.read_csv(_log_file)
            parsed = json.loads(component_logs.head(self.lines_by_components).to_json(orient="records"))
            for log in parsed:
                self.kafka_producer.send(self.kafka_topic, log)
                print(f"Send {self.component_number} log line(s) from file {_log_file} to topic {self.kafka_topic}")

    def producer_metrics(self):
        return self.kafka_producer.metrics()

if __name__ == "__main__":
    log_producer = LogsProducer(kafka_topic="testtopic")
    log_producer.create_kafka_producer()
    log_producer.produce_logs()