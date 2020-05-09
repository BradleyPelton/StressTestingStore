FROM ubuntu:18.04

COPY docker-entrypoint.sh /

RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get install -y git \
    && apt-get install -y python3.8 \
    && apt-get install -y python3-pip \
    && python3 -m pip install --no-cache-dir git+https://github.com/locustio/locust.git@0.13.5#egg=locustio \
    && apt-get clean \
    && mkdir /locust

WORKDIR /locust
EXPOSE 8089 5557 5558


ENTRYPOINT ["/docker-entrypoint.sh"]