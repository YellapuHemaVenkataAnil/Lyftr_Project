#!/bin/bash
source venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --http://localhost:8000
