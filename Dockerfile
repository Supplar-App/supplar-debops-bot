FROM python:3.9
RUN apt-get update -y
RUN apt-get upgrade -y

WORKDIR /app/sup_dev_bot

COPY ./requirements.txt ./
RUN pip install -r requirements.txt
COPY ./ ./

CMD ["python3", "src/bot.py"]