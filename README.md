# BioShock: Biomaterial Monitoring System

## Overview
BioShock is a Python-based program designed to monitor biomaterials using an array of cameras and sensors. This system enables real-time data collection, image capture, and analysis to provide comprehensive insights into the behavior of biomaterials under various conditions.

## Key Features
1. Multi-Sensor Integration: BioShock integrates a variety of sensors, including temperature and humidity.

2. Imaging: BioShock captures high-quality images of biomaterial samples using webcams or the pi camera, allowing researchers to observe minute changes and structural developments.

3. Automated Data Collection: With its defined interval functionality, BioShock automatically takes multiple images over a specific timeframe, reducing manual effort and ensuring continuous monitoring.

4. Time-Lapse Generation: By leveraging the collected images, BioShock generates visually insightful time-lapses, enabling users to visualize and analyze the biomaterial's behavior over time.

## Hardware
- Raspberry Pi 4 (will create a fork that supports 3)
- Humidity Sensor
- Pi Camera or webcam

## Dependencies
- Python 3
- Blinka
- Adafruit

## Usage
1. Run monitoring.py
2. Run timelapse.py