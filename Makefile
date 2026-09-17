PYTHON ?= python3
LATEX ?= pdflatex

.PHONY: analysis slides all
all: analysis slides

analysis:
	$(PYTHON) analysis/discrete_model.py

slides:
	$(LATEX) -interaction=nonstopmode -halt-on-error presentation.tex
	$(LATEX) -interaction=nonstopmode -halt-on-error presentation.tex
