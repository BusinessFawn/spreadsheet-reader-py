# Getting Started

## Env Setup
### Dependencies
* [homebrew](https://brew.sh/) is the easy way
* git
  * `brew install git`
* Python 3.10 
  * `brew install python@3.10`
* virtual environment
  * `python3 -m pip3 install virtualenv`
### Setup
* Setup GitHub (I like [SSH](https://docs.github.com/en/authentication/connecting-to-github-with-ssh/generating-a-new-ssh-key-and-adding-it-to-the-ssh-agent))
* `mkdir ~/git`
* `cd ~/git`
* `git clone git@github.com:BusinessFawn/spreadsheet-reader-py.git`
* `mkdir ~/venv`
* `python3 -m venv ~/venv/spreadsheet-reader-py`
* `source ~/venv/spreadsheet-reader-py/bin/activate`
* `pip install -r requirements.txt`

## Run It
* `cd ~/git/spreadsheet-reader-py`
* `source ~/venv/spreadsheet-reader-py/bin/activate`
* `python main.py`
