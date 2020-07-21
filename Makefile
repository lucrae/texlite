clean:

	# remove all cache files
	find . | grep -E "(__pycache__|\.pyc|\.pyo)" | xargs rm -rf

	# remove example output
	rm -rf examples/*.pdf examples/*.tex

	# remove base-level auxillary/log files
	rm -rf *.out *.aux *.log

flake:

	# Ignore F401 (unused import) and E261 (in-line comments)
	flake8 texlite --extend-ignore F401,E261
	flake8 texlite.py --extend-ignore F401,E261

refresh-git-index:

	# remove all items from git index
	git rm -r --cached .
