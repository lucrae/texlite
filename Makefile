# NB: This is only for development purposes.
# Automated testing goes in tox.ini and .travis.yml

clean:

	# remove all cache files
	find . | grep -E "(__pycache__|\.py[cod]|\.pytest_cache)" | xargs rm -rf

	# remove example output
	rm -rf examples/*.pdf exmaples/*.pdf.swp examples/*.tex

	# remove test output
	rm -rf tests/assets/*.pdf tests/assets/*.pdf.swp tests/assets/*.tex

	# remove base-level auxillary/log files
	rm -rf *.out *.aux *.log

	# remove build/distribution files
	rm -rf build dist *.egg-info

lint:

	# run flake8 style guide checking on source file and setup.py
	flake8 --config setup.cfg

publish:

	# publish package to PyPI
	# DO NOT FORGET TO INCREMENT VERSION IN `texlite._version.py`
	python3 -m pip install --upgrade setuptools wheel twine
	python3 setup.py sdist bdist_wheel
	python3 -m twine upload dist/*
	rm -fr build dist .egg requests.egg-info

refresh-git-index:

	# remove all items from git index
	git rm -r --cached .
