from kafka import KafkaProducer


def send(msg: str, config: dict, event_type: str):
    if event_type == "input_event":
        host = config['kafka']['input']["host"]
        port = config['kafka']['input']["port"]
        topic = config['kafka']['input']["topic"]
        kafka_server = f"""{host}:{port}"""
    else:
        host = config['kafka']['learning']["host"]
        port = config['kafka']['learning']["port"]
        topic = config['kafka']['learning']["topic"]
        kafka_server = f"""{host}:{port}"""

    producer = KafkaProducer(bootstrap_servers=kafka_server)
    producer.send(topic, msg.encode('utf-8'))
    producer.flush()
