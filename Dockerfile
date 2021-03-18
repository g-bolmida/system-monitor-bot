
FROM python:3.10-rc-slim-buster
WORKDIR /root/
COPY discord-bot.py token.env ./
RUN apt update && apt install gcc -y
RUN pip3 install discord && pip3 install psutil
CMD [ "python3", "discord-bot.py" ]