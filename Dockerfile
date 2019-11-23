FROM        python:3.6.8

ENV         LANG C.UTF-8

RUN         set -x \
            && apt-get -qq update \
            && apt-get install -yq python3-dev \
            && apt-get purge -y --auto-remove \
            && rm -rf /var/lib/apt/lists/*

RUN         mkdir /code

RUN         pip install --upgrade pip
ADD         . /code

RUN         pip install --no-cache-dir -r /code/requirements.txt
WORKDIR     /code