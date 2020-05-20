
test-pypi:
	rm -rf dist
	rm -rf *.egg-info
	python setup.py sdist
	twine upload --repository testpypi dist/*

test-pip:
	pip uninstall pyjdbcconnector
	pip install --index-url https://test.pypi.org/simple/ pyjdbcconnector

upload:
	rm -rf dist
	rm -rf *.egg-info
	python setup.py sdist
	twine upload dist/*