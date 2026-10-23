SHELL := /bin/bash
ROOT  := $(abspath $(dir $(lastword $(MAKEFILE_LIST))))
VENV  := $(ROOT)/venv
PY    := $(VENV)/bin/python
PI    := $(VENV)/bin/pyinstaller
APP   := $(ROOT)/dist/Vial.app
BIN   := $(APP)/Contents/MacOS/Vial

.PHONY: help run app open sign clean check

help:
	@echo "make run    Quellcode starten"
	@echo "make app    .app bauen, signieren, starten"
	@echo "make open   App im Finder öffnen"
	@echo "make sign   nur signieren"
	@echo "make clean  build/ und dist/ löschen"

check:
	@test -x "$(PY)" || { echo "venv fehlt"; exit 1; }
	@test -x "$(PI)" || { echo "pyinstaller fehlt: pip install pyinstaller"; exit 1; }

run: check
	$(PY) $(ROOT)/src/main/python/main.py

app: check
	cd $(ROOT) && $(PI) --noconfirm misc/Vial.spec
	$(MAKE) sign
	file "$(BIN)"
	"$(BIN)"

sign:
	@test -d "$(APP)" || { echo "Kein Bundle"; exit 1; }
	xattr -cr "$(APP)"
	codesign --force --deep --sign - "$(APP)"

open: sign
	open "$(APP)"

clean:
	rm -rf "$(ROOT)/build" "$(ROOT)/dist"
