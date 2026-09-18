FROM python:3.11-slim
WORKDIR /app
COPY simple-python.py .
CMD ["python", "simple-python.py"]