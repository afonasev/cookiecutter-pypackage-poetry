import os
import shutil

remove_resources = {
    'travis': [
        '.travis.yml',
    ],
    'github_actions': [
        '.github/workflows',
    ]
}


def remove_resource(resources):
    for resource in resources:
        if os.path.isfile(resource):
            os.remove(resource)
        elif os.path.isdir(resource):
            shutil.rmtree(resource)


def main():
    if "{{ cookiecutter.use_travis }}".lower() not in ('yes', 'y'):
        remove_resource(remove_resources['travis'])

    if "{{ cookiecutter.use_github_actions }}".lower() not in ('yes', 'y'):
        remove_resource(remove_resources['github_actions'])


if __name__ == '__main__':
    main()
