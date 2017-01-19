#!/usr/bin/env bash

# Recommended by official Docker documentation.
# https://docs.docker.com/compose/startup-order/

set -e

host="$1"
shift
cmd="$@"

until psql -h "$host" -U "postgres" -c '\l'; do
      >&2 echo "Postgres is unavailable - sleeping"
        sleep 1
    done

    >&2 echo "Postgres is up - executing command"

exec "run.sh"
