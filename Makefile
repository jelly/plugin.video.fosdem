export PYTHONPATH := $(CURDIR)/resources/lib:$(CURDIR)/tests
PYTHON := python

name = $(shell xmllint --xpath 'string(/addon/@id)' addon.xml)
version = $(shell xmllint --xpath 'string(/addon/@version)' addon.xml)
git_branch = $(shell git rev-parse --abbrev-ref HEAD)
git_hash = $(shell git rev-parse --short HEAD)

zip_name = $(name)-$(version)-$(git_branch)-$(git_hash).zip

include_files = addon.py addon.xml LICENSE.txt README.md resources/
include_paths = $(patsubst %,$(name)/%,$(include_files))
exclude_files = \*.new \*.orig \*.pyc \*.pyo
zip_dir = $(name)/

languages = $(filter-out en_gb, $(patsubst resources/language/resource.language.%, %, $(wildcard resources/language/*)))

path := /

blue = \e[1;34m
white = \e[1;37m
reset = \e[0;39m

all: check test build
zip: build
test: check test-unit test-run

check: check-tox check-pylint check-translations check-codecov

check-tox:
	@echo -e "$(white)=$(blue) Starting sanity tox test$(reset)"
	$(PYTHON) -m tox -q

check-pylint:
	@echo -e "$(white)=$(blue) Starting sanity pylint test$(reset)"
	$(PYTHON) -m pylint resources/lib/ tests/

check-translations:
	@echo -e "$(white)=$(blue) Starting language test$(reset)"
	@-$(foreach lang,$(languages), \
		msgcmp resources/language/resource.language.$(lang)/strings.po resources/language/resource.language.en_gb/strings.po; \
	)

check-addon: clean
	@echo -e "$(white)=$(blue) Starting sanity addon tests$(reset)"
	kodi-addon-checker . --branch=krypton
	kodi-addon-checker . --branch=leia

check-codecov:
	@echo -e "$(white)=$(blue) Test codecov.yml syntax$(reset)"
	@curl --data-binary @codecov.yml https://codecov.io/validate

unit: test-unit
run: test-run

test-unit: clean
	@echo -e "$(white)=$(blue) Starting unit tests$(reset)"
	$(PYTHON) -m unittest discover -v

test-run:
	@echo -e "$(white)=$(blue) Run CLI$(reset)"
	$(PYTHON) tests/run.py $(path)

build: clean
	@echo -e "$(white)=$(blue) Building new package$(reset)"
	@rm -f ../$(zip_name)
	cd ..; zip -r $(zip_name) $(include_paths) -x $(exclude_files)
	@echo -e "$(white)=$(blue) Successfully wrote package as: $(white)../$(zip_name)$(reset)"

clean:
	@echo -e "$(white)=$(blue) Cleaning up$(reset)"
	find . -name '*.py[cod]' -type f -delete
	find . -name '__pycache__' -type d -delete
	rm -rf .pytest_cache/ .tox/
	rm -f *.log tests/userdata/tokens/*.tkn
