#! /bin/bash

curl \
    -H "Authorization: Bearer eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJ0b2tlbl90eXBlIjoiYWNjZXNzIiwiZXhwIjoxNjU1MjA2NTU4LCJpYXQiOjE2NTUxOTkzNTgsImp0aSI6ImEzNWNkOGMzNjgxMDQ4NDhiZTE0M2FmNDY5ZWFlZjkyIiwidXNlcl9pZCI6IjRCdTBzT0JJc1NGMExqT1oyZVlZeExNalQ5NmFVU1RGIn0.PNDZop_iVI1UG5HwcPAmqcgvC5JieWcbYdSdWUUlke8" \
    -H "Content-Type: application/json" -d '
    {
        "category": "Beds", 
        "id_product": "T-01", 
        "stock": 32, 
        "height": 23, 
        "width": 43, 
        "depth": 54, 
        "cost": 50000, 
        "material": "Plastic"
    }' \
    http://127.0.0.1:8000/api/predict/
