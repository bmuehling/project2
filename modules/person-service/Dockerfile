FROM python:3.11-slim

WORKDIR .

#RUN apk add --no-cache gcc musl-dev linux-headers geos libc-dev postgresql-dev postgresql-libs

COPY requirements.txt .
RUN pip install --upgrade pip \
 && pip install --no-cache-dir -r requirements.txt

EXPOSE 5011

COPY . .
CMD ["flask", "run", "--host", "0.0.0.0", "--port", "5011"]