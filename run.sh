#!/bin/sh
source venv/bin/activate
clear
uvicorn server:app --reload --port 2323 --host "0.0.0.0"