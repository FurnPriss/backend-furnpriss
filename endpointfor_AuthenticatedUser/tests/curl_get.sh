#!/bin/bash
curl \
    -X GET \
    -H "Authorization: Bearer [PASTED_YOUR_BEARER_TOKEN_HERE]" \
    http://127.0.0.1:8000/api/authenticated/endpoint
