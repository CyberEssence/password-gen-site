# not yet working

FROM python:3.11

WORKDIR /passgen

COPY requirements.txt .

RUN apt-get update && apt-get install libsasl2-dev libldap-dev libssl-dev
RUN pip install python-ldap
RUN pip install pyOpenSSL
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
