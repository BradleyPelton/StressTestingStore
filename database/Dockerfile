FROM ubuntu:18.04

RUN    apt-get update \
    && apt-get install -y --no-install-recommends \
    && apt-get install -y postgresql \
    && apt-get install sudo -y \
    && apt-get clean \
    && mkdir /postgresdir

WORKDIR /postgresdir

EXPOSE 8089 5557 5558 5432