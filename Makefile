.PHONY: init test ci coveralls fmt fmtcheck lint dists testupload liveupload

init:
	pip install pipenv --upgrade
	pipenv install --dev --skip-lock

test:
	pipenv run tox -p auto

ci:
	pipenv run pytest --cov=telnyx

coveralls:
	pipenv run coveralls

fmt:
	pipenv run tox -e fmt

fmtcheck:
	pipenv run tox -e fmt -- --check --verbose

lint:
	pipenv run tox -e lint

dists:
	rm -rf dist
	pipenv run python setup.py sdist bdist_wheel

testupload:
	# upload keys held in lastpass; save the file to ~/.pypirc-telnyx
	test -f ~/.pypirc-telnyx
	pipenv run twine upload \
		--config-file ~/.pypirc-telnyx \
		--repository test \
		dist/*
	echo "Check for publishing: https://test.pypi.org/project/telnyx/"
	echo "Check installable   : pip install -U -i https://test.pypi.org/simple/ telnyx"

liveupload:
	test -f ~/.pypirc-telnyx
	pipenv run twine upload \
		--config-file ~/.pypirc-telnyx \
		--repository live \
		dist/*
	echo "Check for publishing: https://pypi.org/project/telnyx/"
	echo "Check installable   : pip install -U telnyx"
