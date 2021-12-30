clean-pycache:
	find . | grep -E "(__pycache__|\.pyc|\.pyo$$)" | xargs rm -rf
clean-venv:
	find . -type d | grep "venv$$" | xargs rm -rf