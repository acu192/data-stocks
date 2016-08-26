
all:
	@echo 'make download      # download stuff'
	@echo 'make combine       # combine stuff'

download:
	python code/YahooDataGrabber.py code/tickers.txt
	rm -rf data
	mkdir data
	mv *.csv data/

combine:
	python code/Combine.py data/
