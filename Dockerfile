FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install --no-cache -r requirements.txt
ENV PORT=5000
EXPOSE $PORT
ENTRYPOINT python3 app.py
