#!/bin/bash
curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"username": "django", "password": "djangoee"}' \
    http://localhost:8000/api/token/
