'''
This module tests if the save_thread_result package can be
successfully built on different python versions in a
Docker image.
'''

import os

from typing import (
    Sequence,
)

def main():
    dockerfile_template = read_file(['.', 'Dockerfile_template'])
    versions = [
        '3.1.1',
    ]
    for version in versions:
        write_dockerfile(dockerfile_template, version)
    for version in versions:
        build_docker_image(version)


def read_file(
    file_location: Sequence[str]
) -> str:
    formatted_dockerfile_template_location = os.path.join(*file_location)
    with open(file=formatted_dockerfile_template_location, mode='r', buffering=-1, encoding='utf-8', newline=None) as file:
        return file.read()

def write_dockerfile(
    dockerfile_template: str,
    python_version: str,
) -> None:
    formatted_dockerfile_location = os.path.join('.', f'Dockerfile_python{python_version}')
    major_minor                   = '.'.join(python_version.split('.')[:-1:])
    with open(file=formatted_dockerfile_location, mode='w', buffering=-1, encoding='utf-8', newline=None) as file:
        file.write(dockerfile_template.format(FULL_VERSION=python_version, MAJOR_MINOR=major_minor))

def build_docker_image(
    python_version: str,
) -> None:
    pass


if __name__ == '__main__':
    main()
