# Terminal Farm

## What is it?
An ascii farming simulator created for the itch.io [Terminal Jam](https://itch.io/jam/terminal-jam)

## Installation

### Linux
* Add python 3.7 ppa repo `sudo add-apt-repository ppa:jonathonf/python-3.7 && sudo apt-get update`
* Install python 3.7 `sudo apt-get install python3.7`
* Add an alias for python 3.7 to your bashrc (if you want) `alias python=/usr/bin/python3.7`
    * Make sure you `source ~/.bashrc`
* Add an alias for pip to your bashrc (if you want) `alias pip='python -m pip'`
    * Make sure you `source ~/.bashrc`
* Upgrade python 3.7's pip `python -m pip install --upgrade pip`
* Install pipenv `pip install pipenv` (may already be installed)
* Add an alias for pipenv to your bashrc `alias pipenv='python -m pipenv'`
    * Make sure you `source ~/.bashrc`
    * Alternativly you can add some folder to your path (~/.local  ?), I don't know how
* Install dependencies with pipenv `pipenv install`
 

### Windows
* Install python 3.7.1
* Install pip (Hopefully already have it with python install)
* get pipenv `pip install pipenv`
* install dependencies with `pipenv install`

## Running

* For once of running of the game use `pipenv run python game.py`
* To run an interactive shell run `pipenv shell`
    * **This appears to not work on Linux!:** I'm having issues with the path not appropriately 
    being set when running the shell, therefore resulting in python not being able to find imports
    * To run the game from the shell use `python game.py`


## Other important things
* Ensure you're using flake8 to enforce style `flake8 .`
    * vscode plugins can automatically highlight style errors on save
* autopep8 can be used with your editor to auto format
    * You can do this manually in vscode by using `shift+alt+f`
    * You can automatically format on save by setting `preferences -> settings -> text editor -> formatting -> format on save`
* To enforce typing you can run `mypy .`
    * To get vscode to automatically do type checking you need to enable the work space setting `"python.linting.mypyEnabled": true,`