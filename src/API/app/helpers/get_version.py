import os


def current_app_version(version_file):
    version = open(version_file).read()
    return version.strip()