FROM python:3.10.11-slim

# ENV http_proxy http://proxy-chain.xxx.com:911/
# ENV https_proxy http://proxy-chain.xxx.com:912/ 

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install --default-timeout=100 -r requirements.txt

COPY . .

# CMD ["python", "app.py"]
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]