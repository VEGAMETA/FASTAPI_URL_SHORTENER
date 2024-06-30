#!/bin/sh
source venv/bin/activate
clear
uvicorn server:app --reload