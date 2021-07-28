# Docker file to build an ATUA API image.
# Please, setup the ENVIRONMENT variable by parameters.

FROM amancevice/pandas:1.3.1-slim

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

# Install requirements
    RUN python3 -m pip install --upgrade setuptools cython\
        && python3 -m pip install \
            -r /requirements_base.txt \
            -r /requirements_${ENVIRONMENT}.txt


EXPOSE "8000:8000"
CMD ["sh", "deploy.sh"]

