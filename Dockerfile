FROM python:3.10-slim

RUN apt-get update && apt-get install -y git

RUN pip install openvino==2024.1.0 openvino-dev==2024.1.0 optimum-intel[openvino] transformers

WORKDIR /workspace
