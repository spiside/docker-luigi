#!/usr/bin/env python
"""
Reads from environment variables and generates the luigi
config file to /etc/luigi/client.cfg using python's configparser.

Environment variables to be written should follow this standard:

    LUIGI_<section>_<key>=<value>

eg.
    LUIGI_CORE_DEFAULT-SCHEDULER-URL=http://localhost:8082
        ->
            [core]
            default-scheduler-url=http://localhost:8082

    LUIGI_WORKER_PING_INTERNAL=1.0
        ->
            [worker]
            ping_internal=1.0

"""
import configparser
import os

# This file is the first config file to be read based on luigi documentation.
# It is lowest in priority so it is possible to overwrite values in the other
# config files.
# http://luigi.readthedocs.io/en/stable/configuration.html
FILENAME = '/etc/luigi/luigi.cfg'
LUIGI_BLACKLIST = ('LUIGI_CONFIG_PATH',)
SPECIAL_CONFIG = ('batch_notifier', 'task_history', 'execution_summary')


def environment_to_config(env=os.environ):
    config = configparser.ConfigParser()
    for variable, value in env.items():
        if not variable.startswith('LUIGI') or variable in LUIGI_BLACKLIST:
            continue
        _, variable = variable.lower().split('_', 1)

        if any(variable.startswith(s) for s in SPECIAL_CONFIG):
            split = variable.split('_', 2)
            section, key = "_".join((split[0], split[1])), split[-1]
        else:
            section, key = variable.split('_', 1)

        if not config.has_section(section):
            config.add_section(section)

        config.set(section, key, value)

    return config


if __name__ == '__main__':
    config = environment_to_config()
    os.makedirs(os.path.dirname(FILENAME), exist_ok=True)

    with open(FILENAME, 'w') as f:
        config.write(f, space_around_delimiters=False)
