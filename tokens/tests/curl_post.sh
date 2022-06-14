#!/bin/bash
curl \
    -X POST \
    -H "Content-Type: application/json" \
    -d '{"email": "django@django.com", "password": "djangoee"}' \
    http://localhost:8000/api/token/
