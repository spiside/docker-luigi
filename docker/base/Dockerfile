# Base luigi Dockerfile with python3.5.2
FROM python:3.5.2
MAINTAINER Spiro Sideris <spirosideris at gmail.com>

# Run an update, create a luigi user with sudo permissions, and install
# python tools for luigi.
RUN DEBIAN_FRONTEND=noninteractive && \
    apt-get -q update && \
    useradd --password NP --create-home --shell /bin/bash luigi && \
    apt-get install -q -y --no-install-recommends \
        sudo cron python-dev libpq-dev build-essential \
        postgresql-client \
    && \
    echo "luigi ALL=(ALL) NOPASSWD:ALL" >> /etc/sudoers && \
    apt-get clean && \
    rm -rf /var/lib/apt/lists/*

# Install the luigi package and the database requirements for postgres task
# history.
RUN pip install 'luigi==2.4.0' 'sqlalchemy==1.1.0' 'psycopg2==2.6.2'
RUN mkdir /etc/luigi && chmod -R a+rw /etc/luigi

COPY scripts/ .
RUN chmod +x generate_config.py && chmod +x run.sh && mv run.sh /usr/bin

USER luigi

CMD ["run.sh"]
