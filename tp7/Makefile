MATERIA := $(notdir $(abspath $(CURDIR)/..))
TP := $(notdir $(CURDIR))
OUTPUT_NAME := $(MATERIA)_$(TP)

SRC := main.tex

all:
	latexmk -pdf -jobname=$(OUTPUT_NAME) $(SRC)

clean:
	latexmk -c -jobname=$(OUTPUT_NAME) $(SRC)
	rm -f *.bbl *.run.xml *.synctex.gz

distclean:
	latexmk -CA -jobname=$(OUTPUT_NAME) $(SRC)
	rm -f *.bbl *.run.xml *.synctex.gz
