
all:
	@echo 'make download      # download stuff'
	@echo 'make combine       # combine stuff'

download:
	python YahooDataGrabber.py tickers.txt
	rm -rf data
	mkdir data
	mv *.csv data/

combine:
	python Combine.py data/
