# Structured Logging Project

## Overview
This project demonstrates JSON structured logging for a backend service.

## Features
- JSON formatted logs
- Includes timestamp, service name, log level, and message
- Works inside Docker container

## Run Locally
```bash
pip install -r requirements.txt
python app.py
```

## Run with Docker
```bash
docker build -t structured-logging .
docker run -p 5000:5000 structured-logging
```
