#!/usr/bin/env python
import os, sys
from .sensors_main import launch_sensors

def startDjango(settings_path='tipboard.webserver.settings'):
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', settings_path)
    sys.path.insert(0, os.getcwd())  # Import project to PYTHONPATH
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


def show_help():
    help = """Usage:
  -h, or help  \t\t=> show help usage
  -r, or runserver\t=> start the tipboard server
  -s, or sensors \t=> start sensors located in src/sensors
                """
    print(help)
    return 0


def main(argc, argv):  # don't you miss the old fashion way, the fabulous main in C :D.    I do
    exitStatus = -42
    if argc == 2 and "help" in argv[1] or '-h' in argv[1]:
        exitStatus = show_help()
    elif argc == 2 and "sensors" in argv[1] or '-s' in argv[1]:
        exitStatus = launch_sensors()
    elif argc >= 2 and ("runserver" in argv[1] or "test" in argv[1]):
        exitStatus = startDjango()
    return exitStatus


def main_as_pkg():
    """ to become a python package and go to pypi, started in ../setup.py """
    return startDjango(settings_path='src.tipboard.webserver.settings')


if __name__ == '__main__':
    main(len(sys.argv), sys.argv)
