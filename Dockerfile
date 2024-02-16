FROM python:3.6-alpine
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
WORKDIR /art
COPY . .
RUN pip install -r requirements.txt
EXPOSE 80
ENTRYPOINT ["python", "manage.py"]
CMD ["runserver", "0.0.0.0:80"]
