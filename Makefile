clean:

	# remove cache files
	rm -rf **/__pycache__ **/.pytest_cache

	# remove example output
	rm -rf examples/*.pdf examples/*.tex

remove-git-cache:

	# remove all from index
	git rm -r --cached .
