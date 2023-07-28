VENV = venv
SRC = src
PIP = $(VENV)/bin/pip
PYTHON = $(VENV)/bin/python3
REQ_FILE = requirements.txt

install: $(VENV)/bin/activate
	$(PIP) install -r $(REQ_FILE)

run: $(VENV)/bin/activate
	$(PYTHON) $(SRC)/main.py $(ARGS)

sweep: $(VENV)/bin/activate
	$(PYTHON) $(SRC)/main.py s

$(VENV)/bin/activate: $(REQ_FILE)
	test -d $(VENV) || python3 -m venv $(VENV)
	$(PIP) install --upgrade pip
	touch $(VENV)/bin/activate

clean:
	rm -rf __pycache__
	rm -rf "Simulation Results"
