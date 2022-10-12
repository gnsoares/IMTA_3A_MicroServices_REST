FROM python:3.10.5-alpine
WORKDIR /app
COPY requirements.txt /app
RUN pip install -r requirements.txt
ADD . /app/
CMD ["python","-u","booking.py", "-H", "0.0.0.0", "-p", "3201"]
