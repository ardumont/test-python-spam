PYTHON = python3
SETUP = $(PYTHON) setup.py

all: build

build:
	$(SETUP) build

clean::
	$(SETUP) clean
	rm -f *.so *.o *.pyc
	rm -rf build
