#### Terminal Farm

## What is it?
An ascii farming simulator created for the itch.io [Terminal Jam](https://itch.io/jam/terminal-jam)

## Installation
* Install python 3.7.1
* Install pip (Hopefully already have it with python install)
* get pipenv `pip install pipenv`
* install dependencies with `pipenv install`
* Start the shell environment with `pipenv shell`
* Run the game with `python game.py`

## Other important things
* Ensure you're using flake8 to enforce style `flake8 .`
    * vscode plugins can automatically highlight style errors on save
* autopep8 can be used with your editor to auto format
    * You can do this manually in vscode by using `shift+alt+f`
    * You can automatically format on save by setting `preferences -> settings -> text editor -> formatting -> format on save`
* To enforce typing you can run `mypy .`
    * To get vscode to automatically do type checking you need to enable the work space setting `"python.linting.mypyEnabled": true,`