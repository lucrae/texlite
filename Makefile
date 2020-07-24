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

lint:

	# run flake8 style guide checking on source file and setup.py
	flake8 --config setup.cfg texlite setup.py

refresh-git-index:

	# remove all items from git index
	git rm -r --cached .
