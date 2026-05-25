# Setup Guide

## Requirements

- Python 3.10+
- MQTT Broker
- ESP32
- Node-RED
- Grafana

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Run MQTT Publisher

```bash
python src/mqtt_publisher.py
```

---

## Run MQTT Subscriber

```bash
python src/mqtt_subscriber.py
```

---

## Project Structure

```text
industrial-iot-monitoring/
│
├── src/
│   ├── mqtt_publisher.py
│   └── mqtt_subscriber.py
│
├── docs/
│   └── setup.md
│
├── requirements.txt
├── .gitignore
└── README.md
```
