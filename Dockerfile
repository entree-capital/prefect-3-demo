FROM --platform=linux/amd64 prefecthq/prefect:3.0.0rc10-python3.11
COPY . .
COPY flows /opt/prefect/flows

# COPY requirements.txt requirements.txt
# RUN pip install -r requirements.txt