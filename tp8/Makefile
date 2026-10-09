MATERIA := $(notdir $(abspath $(CURDIR)/..))
TP := $(notdir $(CURDIR))
OUTPUT_NAME := $(MATERIA)_$(TP)

SRC := main.tex

all:
	latexmk -pdf -interaction=nonstopmode -jobname=$(OUTPUT_NAME) $(SRC)

clean:
	latexmk -CA -jobname=$(OUTPUT_NAME) $(SRC)
