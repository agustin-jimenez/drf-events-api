# Docker file to build an ATUA API image.
# Please, setup the ENVIRONMENT variable by parameters.

FROM python:3.9-alpine

LABEL mantainer="Agustin Jimenez"\
      version="1.0.0"\
      description="Events tracker API"

# Environment vars
    ARG ENVIRONMENT=development
    ENV PYTHONUNBUFFERED 1
    ENV LIBRARY_PATH=/lib:/usr/lib

 
# Add directories and files
    RUN mkdir /src
    ADD ./src/ /src/
    WORKDIR /src
    ADD ./requirements/base.txt /requirements_base.txt
    ADD ./requirements/${ENVIRONMENT}.txt /requirements_${ENVIRONMENT}.txt

# Installing postgress support, requirements and delete cache.
    RUN apk add \
            --update \
            --no-cache \
            postgresql-client \
            jpeg-dev \
            zlib-dev \
            py3-requests \
            curl-dev \
            libressl-dev \
        && apk add \
            --update \
            --no-cache \
            --virtual \
            .tmp-build-deps \
            gcc g++ libc-dev \
            linux-headers \
            postgresql-dev \
        && pip install \
            -r /requirements_base.txt \
            -r /requirements_${ENVIRONMENT}.txt \
        && apk del .tmp-build-deps 

EXPOSE "8000:8000"
CMD ["sh", "deploy.sh"]
