# Alternate base image layer:
#FROM debian:buster-slim

FROM ubuntu:18.10

ENV DEBIAN_FRONTEND noninteractive

RUN apt-get update && \
    apt-get -y install --no-install-recommends \
      gettext \
      make \
      python3 \
      python3-setuptools \
      python3-babel \
      python3-jinja2 && \
    apt-get clean all && \
    apt-get -y autoremove && \
    rm -rf \
      /var/lib/apt/lists/* \
      /tmp/*

CMD /bin/bash -c "cd /tmp/ && make"
