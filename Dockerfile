FROM python:3.6-alpine
COPY . /grpc
RUN pip install -r requirements.txt
EXPOSE 50051

CMD [ "python", "./server.py" ]