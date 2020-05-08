


# THE IMAGE I'M USING:
# https://hub.docker.com/r/grubykarol/locust

# BELOW IS A COPY OF THAT DOCKER FILE FOR REFERENCE 




#   Copyright 2019 Karol Brejna
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
FROM python:3.8.1-alpine3.11

COPY docker-entrypoint.sh /

RUN    apk --no-cache add --virtual=.build-dep build-base git \
    && apk --no-cache add zeromq-dev libffi-dev \
    && python3 -m pip install --no-cache-dir git+https://github.com/locustio/locust.git@0.13.5#egg=locustio  \
    && apk del .build-dep \
    && chmod +x /docker-entrypoint.sh \
    && mkdir /locust
WORKDIR /locust
EXPOSE 8089 5557 5558

ENTRYPOINT ["/docker-entrypoint.sh"]