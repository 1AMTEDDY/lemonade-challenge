import os
import time
import requests
from prometheus_client import start_http_server, Gauge

RABBITMQ_HOST = os.getenv("RABBITMQ_HOST", "http://localhost:15672")
RABBITMQ_USER = os.getenv("RABBITMQ_USER", "guest")
RABBITMQ_PASSWORD = os.getenv("RABBITMQ_PASSWORD", "guest")

# Prometheus Gauges
g_messages = Gauge(
    "rabbitmq_individual_queue_messages",
    "Total messages in the queue",
    ["host", "vhost", "name"]
)

g_messages_ready = Gauge(
    "rabbitmq_individual_queue_messages_ready",
    "Messages ready in the queue",
    ["host", "vhost", "name"]
)

g_messages_unack = Gauge(
    "rabbitmq_individual_queue_messages_unacknowledged",
    "Messages unacknowledged in the queue",
    ["host", "vhost", "name"]
)

def collect_rabbitmq_metrics():
    url = f"{RABBITMQ_HOST}/api/queues"
    try:
        response = requests.get(url, auth=(RABBITMQ_USER, RABBITMQ_PASSWORD))
        response.raise_for_status()
        queues = response.json()

        for queue in queues:
            vhost = queue.get("vhost", "")
            name = queue.get("name", "")
            messages = queue.get("messages", 0)
            messages_ready = queue.get("messages_ready", 0)
            messages_unack = queue.get("messages_unacknowledged", 0)

            # Set gauge values
            g_messages.labels(RABBITMQ_HOST, vhost, name).set(messages)
            g_messages_ready.labels(RABBITMQ_HOST, vhost, name).set(messages_ready)
            g_messages_unack.labels(RABBITMQ_HOST, vhost, name).set(messages_unack)

    except Exception as e:
        print(f"Error collecting metrics: {e}")

if __name__ == "__main__":
    start_http_server(8000)
    print("Starting RabbitMQ Prometheus Exporter on port 8000...")
    while True:
        collect_rabbitmq_metrics()
        time.sleep(5)