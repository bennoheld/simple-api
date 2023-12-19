# Use an official Python runtime as the base image
FROM python:3.11-slim

RUN apt update && apt install -y curl && apt-get clean

RUN adduser --system --home /home/worker worker
COPY --chown=worker ./src /src
COPY --chown=worker ./requirements.txt /src/requirements.txt

USER worker

WORKDIR /src
RUN pip3 install -r ./requirements.txt --user

HEALTHCHECK --interval=20s --timeout=3s \
    CMD curl -f http://localhost:5003/health || exit 1

EXPOSE 5003
ENTRYPOINT ["python3", "/src/app.py"]