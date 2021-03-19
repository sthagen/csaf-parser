SHELL = /bin/bash

.PHONY: all available
all: ; $(info $$var is [${var}])echo Hello world
	@echo "usage: "
	@echo "       make clean - removes output files"

clean:
	@echo "- removing output files"
	@rm -f csaf-parser.log logs/csaf-parser.log
