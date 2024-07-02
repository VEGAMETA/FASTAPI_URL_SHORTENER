call venv\Scripts\activate
cls
uvicorn server:app --reload --port 2323 --host "0.0.0.0"