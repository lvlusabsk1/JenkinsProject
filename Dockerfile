FROM python:3.11-slim
WORKDIR /app
COPY mohammadmusaab.py .
CMD ["python", "mohammadmusaab.py"]