FROM spiside/luigi:latest

# This is the worker Dockerfile that you can use to install worker
# specific packages. Some common ones that I've seen are numpy, scipy,
# and pandas. These are build time expense packages so you might want
# to add these to an intermediate package.
ADD . luigi/
WORKDIR luigi/

RUN pip install -r requirements.txt

ENV PYTHONPATH /luigi
COPY docker/run_worker.sh /usr/bin/run_worker

CMD ["run_worker"]
