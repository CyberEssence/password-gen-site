# not yet working

FROM python:3.11

WORKDIR .

COPY . .

RUN apt-get update && apt-get install -y \
    gcc \
    libc6-dev \
    libssl-dev \
    libldap2-dev \
    libsasl2-dev

RUN pip install python-ldap
RUN pip install pyOpenSSL
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
