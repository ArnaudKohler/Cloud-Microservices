FROM python:3.10
WORKDIR /app
COPY ./* /app
RUN ls -l /app
RUN pip install -r requirements.txt
CMD ["python", "app.py"]