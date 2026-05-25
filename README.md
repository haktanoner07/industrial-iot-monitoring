# Industrial IoT Monitoring System

Real-time environmental monitoring system developed with ESP32, MQTT and Grafana infrastructure.

## 🚀 Technologies

- ESP32
- MQTT
- Node-RED
- InfluxDB
- Grafana
- Python

---

## 📡 Features

- Real-time sensor monitoring
- MQTT communication
- Dashboard visualization
- Embedded system integration
- Data logging infrastructure

---

## 🏗️ System Architecture

```text
+-----------+       +-----------+       +-------------+
|  Sensors  | ----> |   ESP32   | ----> | MQTT Broker |
+-----------+       +-----------+       +-------------+
                                              |
                                              v
                                       +-------------+
                                       |  Node-RED  |
                                       +-------------+
                                              |
                                              v
                                       +-------------+
                                       |  InfluxDB  |
                                       +-------------+
                                              |
                                              v
                                       +-------------+
                                       |   Grafana  |
                                       +-------------+

---

## 📈 Status

Project is under active development.
