
PYTHON := python3
LOCK_VENV := .venv-lock-tools
LOCK_PYTHON := $(LOCK_VENV)/bin/python

.PHONY: install-standards sync-lock sync-lock-dry-run update-standards validate-lock

TARGET ?= .
PROFILE ?=

$(LOCK_PYTHON):
	$(PYTHON) -m venv $(LOCK_VENV)
	$(LOCK_PYTHON) -m pip install --quiet jsonschema

install-standards:
	$(PYTHON) scripts/install_standards.py --target $(TARGET) $(if $(PROFILE),--profile $(PROFILE),)

sync-lock:
	$(PYTHON) scripts/sync_superpowers_lock.py

sync-lock-dry-run:
	$(PYTHON) scripts/sync_superpowers_lock.py --dry-run

update-standards:
	$(PYTHON) scripts/update_standards.py --target $(TARGET) $(if $(PROFILE),--profile $(PROFILE),)

validate-lock: $(LOCK_PYTHON)
	$(LOCK_PYTHON) scripts/validate_upstream_lock.py
