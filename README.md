
**Currently downloaded range:** 2000-01-01 --> 2016-08-01 (inclusive)


### Overview

This repo contains:

1. code to download stock data from Yahoo (based on [this Gist](https://gist.github.com/pmcs/3971115)), and
2. pre-downloaded stock data (downloaded by this code).


### How to use this repo

1. Clone this repo.

2. Run `make combine` to combine all the individual files in the `data/` folder. This command creates a HUGE single file in the root of the repo named `all.csv`.

3. Do something cool with `all.csv`.


### How to download more data

1. Clone this repo.

2. Edit the date range in [YahooDataGrabber.py](code/YahooDataGrabber.py). I.e. Look at the *currently downloaded range* at the top of this file and decide to either download dates prior to this range or after this range -- be sure your chosen range doesn't overlap the *currently downloaded range* as you don't want to get duplicate days!

3. Run `make download` then `make combine`.

