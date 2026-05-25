# Industrial IoT Monitoring System

![Python](https://img.shields.io/badge/Python-3.x-blue)
![ESP32](https://img.shields.io/badge/ESP32-IoT-orange)
![MQTT](https://img.shields.io/badge/MQTT-Protocol-purple)
![Grafana](https://img.shields.io/badge/Grafana-Dashboard-red)
![InfluxDB](https://img.shields.io/badge/InfluxDB-TimeSeries-black)

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
