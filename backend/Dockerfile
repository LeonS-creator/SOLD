'FROM python:3.10\nWORKDIR /app\nCOPY requirements.txt .\nRUN pip install -r requirements.txt\nCOPY . .\nEXPOSE 8000\nCMD ["uvicorn", "app.main:app", "--host=0.0.0.0", "--port=8000"]' 
