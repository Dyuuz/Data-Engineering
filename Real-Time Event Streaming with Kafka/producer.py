from kafka import KafkaProducer
from faker import Faker
import json
import time
import random

# Connect to Kafka (default localhost:9092)
producer = KafkaProducer(
    bootstrap_servers='localhost:9092',
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

fake = Faker()
names = ["Dyuuz", "Alex", "Sam", "Jordan", "Taylor", "Chris", "Amara", "Tunde"]

def send_orders():
    order_id = 1

    while True:
        order_event = {
            "order_id": order_id,
            "user_id": order_id * 10,
            "amount": 100 + order_id
        }
        user_event = {
            "order_id": order_id,
            "user_id": random.randint(1, 1000),
            "name": fake.name()
        }

        # Send to "orders" topic
        producer.send("orders", value=order_event)
        producer.send("users", value=user_event)

        print(f"Produced order event: {order_event}")
        print(f"Produced user event: {user_event}\n")

        order_id += 1
        time.sleep(2)

if __name__ == "__main__":
    send_orders()