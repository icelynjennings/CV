.PHONY: build

build:
	docker build -t sitemap .

test:
	python3 -m unittest test_sitemap.py

coverage:
	coverage run -m unittest test_sitemap.py
	coverage report -m