from kafka import KafkaConsumer
import json

if __name__ == "__main__":
    consumer = KafkaConsumer(
        "registered_user",
        bootstrap_servers='192.168.0.10:9092',
        auto_offset_reset='earliest',
        group_id="consumer-group-a")
    print("starting the consumer")
    for msg in consumer:
        print("Registered User = {}".format(json.loads(msg.value)))
