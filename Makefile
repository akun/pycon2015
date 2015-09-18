SRC_DIR = pycon2015

.PHONY: all install test clean

all:
	make install
	make test
	make clean

install:
	pip install -r requirements.txt

test:
	nosetests -c nose.cfg
	cd $(SRC_DIR)/mysite && python manage.py test

clean:
	find $(SRC_DIR) tests -name '*.pyc' | xargs rm
