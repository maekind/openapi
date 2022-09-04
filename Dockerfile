#  openapi for vimeo dockerfile for generating the image
FROM python:3-slim
LABEL maekind.project.name="Vimeo OpenApi" \
    maekind.project.maintainer="Marco Espinosa" \
    maekind.project.version="1.0" \
    maekind.project.description="Docker image for hosting the Vimeo OpenApi project" \
    maekind.project.email="marco@marcoespinosa.es"

# Setting env variables for Python
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Changing working dir
WORKDIR /web

# Installaing dependancies & configuring django project
COPY requirements.txt .
RUN apt update && apt install -y \ 
    gcc \
    make \
    postgresql-client \
    tk \
    && apt autoremove \
    && pip install -r requirements.txt 

COPY ./backend/ .
COPY docker-entrypoint.sh .

# Finish config & clean
RUN chmod u+x ./docker-entrypoint.sh \
    && rm -Rf /var/cache/apt/* \
    && rm -Rf /var/lib/apt/lists/* \
    && rm requirements.txt

# Set working dir to path
ENV PATH="/web:${PATH}"

# Setting entrypoint
CMD [ "docker-entrypoint.sh" ]
