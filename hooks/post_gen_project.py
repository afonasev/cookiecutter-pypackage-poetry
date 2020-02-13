import os
import shutil

remove_resources = {
    'use_travis': [
        '.travis.yml',
    ],
}


def remove_resource(resources):
    for resource in resources:
        if os.path.isfile(resource):
            os.remove(resource)
        elif os.path.isdir(resource):
            shutil.rmtree(resource)


def main():
    if "{{ cookiecutter.use_travis }}".lower() not in ('yes', 'y'):
        remove_resource(remove_resources['use_travis'])


if __name__ == '__main__':
    main()
