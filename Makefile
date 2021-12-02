.PHONY: dev-setup clean install

venv:
	python -m venv venv

dev-setup: venv
	(. venv/bin/activate && pip install -e .)

clean:
	rm -rf venv
	rm -rf build
	find . -name "*.egg-info*" -exec rm -rv {} +
	find . -name "*__pycache__*" -exec rm -rv {} +

install:
	pip install --user .
