FROM python:3.6

EXPOSE 5001

WORKDIR /app

COPY requirements.txt /app
COPY public.key /app
RUN pip install -r requirements.txt

COPY app.py /app
CMD python app.py
