#! /bin/bash
curl \
    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU1MjE0NDM0LCJpYXQiOjE2NTUyMDcyMzQsImp0aSI6IjA1N2NkZjk4MmM3MzRkOWZiM2E0ZDMxYTY4YTUyZTIwIiwidXNlcl9pZCI6IjRCdTBzT0JJc1NGMExqT1oyZVlZeExNalQ5NmFVU1RGIn0.uF7Aaf7V-i8lKOQJa8RJCt06DMRFTJ-7_hV-v6peIYc" \
    -H 'Content-Type: application/json' \
    -X POST -d '{"added_stock": 32}' \
    http://127.0.0.1:8000/api/products/T-01/stockin.json
