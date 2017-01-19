#!/usr/bin/env bash
set -e

RUN_TYPE=${RUN_TYPE:-worker}


# Generate the luigi config file.
/generate_config.py

case "$RUN_TYPE" in
    worker)
        # Create crontab and give read permissions to luigi.
        env | cat - /luigi/crontab | sudo tee /etc/cron.d/luigi
        sudo chmod 644 /etc/cron.d/luigi

        echo "Running cron in foreground"
        sudo cron -f
        ;;

    dev)
        bash
        ;;

    *)
        echo "Invalid run type: $RUN_TYPE"
        exit 1
        ;;
esac
