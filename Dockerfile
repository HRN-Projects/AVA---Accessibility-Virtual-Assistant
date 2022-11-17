FROM python:latest
LABEL maintainer="Harshawardhan"

RUN apt-get update
RUN apt-get install -y libasound-dev libportaudio2 libportaudiocpp0 portaudio19-dev libsndfile1
RUN apt-get install -y alsa-utils
RUN mkdir /app
RUN useradd -m worker
RUN chown worker /app

#modifying python path and upgrading pip
USER worker
ENV PATH="/home/worker/.local/bin:${PATH}"
RUN python3 -m pip install --upgrade pip

ENV PYTHONUNBUFFERED=1

WORKDIR /app
COPY requirements.txt ./
RUN pip install -r ./requirements.txt
COPY . ./


EXPOSE 5000
CMD ["python3", "AVA.py"]
