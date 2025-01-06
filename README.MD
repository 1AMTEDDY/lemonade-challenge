# DevOps Challenge – Section 2

This repository contains solutions for the **Section 2 Coding Challenges** of the DevOps Assessment.

## Contents

- [DevOps Challenge – Section 2](#devops-challenge--section-2)
  - [Contents](#contents)
  - [1. Prometheus Exporter (RabbitMQ)](#1-prometheus-exporter-rabbitmq)
    - [How to Run](#how-to-run)
  - [2. Script to Restart Laravel (CPU Monitor)](#2-script-to-restart-laravel-cpu-monitor)
    - [How to Run](#how-to-run-1)
  - [3. Postgres Query Troubleshooting Approach](#3-postgres-query-troubleshooting-approach)
  - [4. Dockerfile for Laravel](#4-dockerfile-for-laravel)

---

## 1. Prometheus Exporter (RabbitMQ)

- **Location**: `exporter/rabbitmq_exporter.py`
- **Purpose**: Connects to RabbitMQ Management API and exposes metrics for Prometheus.

### How to Run

1. **Install dependencies**:

   ```bash
   pip install prometheus_client requests

2. **Set environment variables**:

```export RABBITMQ_HOST="http://your-rabbitmq-host:15672"
export RABBITMQ_USER="guest"
export RABBITMQ_PASSWORD="guest"
```

Install RabbitMQ with Homebrew

 1. Install RabbitMQ:

brew install rabbitmq

Start RabbitMQ and Enable Management
Start RabbitMQ in the background as a service:

```brew services start rabbitmq```

 1. Enable the Management Plugin:

```rabbitmq-plugins enable rabbitmq_management```

This plugin provides a web interface to manage RabbitMQ queues and messages.

3. **Create a Queue and Publish a Message**

3.1 Access the RabbitMQ Management Console

 1. Open your browser and navigate to:

<http://localhost:15672>

 2. Log in with the default credentials:
 • Username: guest
 • Password: guest

3.2 Create a Queue

 1. In the top navigation, click “Queues”.
 2. Click the “Add a new queue” button.
 3. Enter the queue name, for example, test-queue.
 4. Click “Add queue”.

3.3 Publish a Message to the Queue

 1. Select test-queue from the list of queues.
 2. Scroll down to the “Publish message” section.
 3. Enter a message in the Payload field, such as:

```Hello from RabbitMQ!```

 4. Click “Publish message”.
 5. The queue details page will update, showing Messages Ready incremented.

 6. Look for metrics related to the queue test-queue, such as:

rabbitmq_individual_queue_messages{host="<http://localhost:15672",vhost="/",name="test-queue"}> 1.0

4. **Access metrics**:

```Open http://localhost:8000/metrics in your browser.
```

## 2. Script to Restart Laravel (CPU Monitor)

- **Location**: `scripts/restart_laravel.sh`
- **Purpose**: Monitors CPU usage every 30 seconds and restarts the Laravel service if usage exceeds 80%.

### How to Run

1. **Make the script executable**:

```chmod +x scripts/restart_laravel.sh
```

2. **Run in the background (optional)**:

```
nohup ./scripts/restart_laravel.sh &
```

3. **Customize**:
 • Update SERVICE_NAME in the script to match your Laravel systemd service name.
 • Change THRESHOLD to the desired CPU usage level.

## 3. Postgres Query Troubleshooting Approach

- **Location**: docs/postgres_troubleshooting.md
- **Purpose**: Outlines steps to diagnose and resolve slow queries.

Key Steps

1. EXPLAIN (ANALYZE) to examine query plan.
2. Index Check for columns used in JOINs, WHERE, or ORDER BY.
3. VACUUM / ANALYZE to keep table stats current.
4. Refactor queries or consider table partitioning if datasets are very large.

For deeper instructions, see postgres_troubleshooting.md.

## 4. Dockerfile for Laravel

- **Location**: docker/Dockerfile
- **Purpose**: Containerize a Laravel app using PHP-FPM + Nginx (or just PHP-FPM if you prefer splitting containers).

How to Build and Run

1. Copy your Laravel project into the repo (or adjust paths in Dockerfile accordingly).
2. Build the image:

```
cd docker
docker build -t my-laravel-app .
```

3. Run the container:

```
docker run -p 80:80 my-laravel-app
```

4. Visit <http://localhost> in your browser (assuming Laravel’s public/ folder is set as doc root).

Additional Notes

- You may need environment variables for database connections (e.g., DB_HOST, DB_USERNAME, DB_PASSWORD).
- If using Supervisor and Nginx in the same container, ensure you have nginx.conf and supervisor.conf in the docker/ folder and that they are copied in the Dockerfile.
