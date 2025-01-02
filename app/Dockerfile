FROM python:3.11.6
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
ENV PATH="/PY/BIN:$PATH"


WORKDIR /app

RUN pip install --upgrade pip

COPY requirements.txt /app/requirements.txt

COPY . /app

COPY ../alembic.ini /app/alembic.ini

RUN pip install -r requirements.txt

 RUN DEBIAN_FRONTEND=noninteractive apt-get install -y \
     libpq-dev \
     gcc \
     && apt-get clean && rm -rf /var/lib/apt/lists/*

EXPOSE 8000
CMD ["alembic" ,"revision" ,"--autogenerate" ,"-m" ,"your message here"]
CMD ["alembic" ,"upgrade" ,"head"]
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000", "--reload"]