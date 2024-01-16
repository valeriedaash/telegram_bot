FROM python:3.10-slim
ENV TOKEN='6896999267:AAFLm3bSifaXtN01SFyuNS9ydbB2yueBL3k'
COPY . .
RUN pip install -r requirements.txt
CMD python bot.py