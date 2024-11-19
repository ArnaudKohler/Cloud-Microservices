FROM python:3.7-slim
WORKDIR /app
COPY ./* /app
RUN ls -l /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]