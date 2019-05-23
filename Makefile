update_example:
	cookiecutter --overwrite-if-exists --no-input --config-file example.yaml .

precommit_install:
	echo '#!/bin/sh\nmake update_example\n' > .git/hooks/pre-commit
	chmod +x .git/hooks/pre-commit
