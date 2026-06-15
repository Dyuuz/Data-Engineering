from kafka import KafkaConsumer
import json

# Connect to Kafka and listen to "orders"
consumer = KafkaConsumer(
    bootstrap_servers='localhost:9092',
    auto_offset_reset='earliest',  # read from beginning
    enable_auto_commit=True,
    group_id='order-group',
    value_deserializer=lambda x: json.loads(x.decode('utf-8'))
)
consumer.subscribe(['orders', 'users'])  # Listen to both topics

print("Listening for messages...\n")

for message in consumer:
    if message.topic == "orders":
        print(f"Received order event: {message.value}")
    elif message.topic == "users":
        print(f"Received user event: {message.value}\n")