# GeoSoil Monitoring System

An IoT-based soil monitoring and analysis system using MQTT, Python backend, MongoDB, and Flutter frontend.

## Project Description

GeoSoil is a smart agriculture monitoring system that collects real-time sensor data using IoT devices and sends it via MQTT to a Python backend. The data is stored in MongoDB and displayed using a Flutter mobile application.

##  Technologies Used

- Python (FastAPI)
- MQTT (HiveMQ Broker)
- MongoDB
- Flutter
- IoT Sensors (Soil, Temperature, Humidity, NPK)
- ESP32

##  Project Structure
codes~
├── client_flutter
└── server_python
├── mqtt_service.py
├── main.py
├── database.py
├── models.py
├── routes.py
├── requirements.txt
