# This file configures the behavior of the shove daemon.
# You should copy it to settings.py and customize it to your needs.
import os


# Change this to point to the root directory under which your projects are stored to make
# generating file paths a little easier.
ROOT = os.path.dirname(__file__)


def path(*args):
    """Utility for making file paths relative to ROOT."""
    return os.path.join(ROOT, *args)


# RabbitMQ connection settings.
RABBITMQ_HOST = 'localhost'
RABBITMQ_PORT = 5672
RABBITMQ_VHOST = '/'
RABBITMQ_USER = 'guest'
RABBITMQ_PASS = 'guest'

# Settings for the periodic heartbeat back to Captain.
HEARTBEAT_QUEUE = 'captain_heartbeat'
HEARTBEAT_DELAY = 5 * 60  # Seconds

# Map of projects that shove can run commands for. Keys are IDs that captain needs to know about,
# values are the path to the repo root directory. Shove expects to find a file under
# `bin/commands.procfile` in each directory here.
PROJECTS = {
    'test_project': path('tests', 'test_project'),
}
