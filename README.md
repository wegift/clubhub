# clubhub

Custom integrations between GitLab and Clubhouse

## Install

I've used this project to try out [Poetry](https://python-poetry.org/) at WeGift. You'll need that first.

```
sudo apt-get install python3.8-venv
sudo pip install -U poetry
```

Then install project deps, poetry handles the virtualenv creation for you.

```
poetry install
```

## Dependancy management

Heroku does not yet support Poetry, we need to maintain a lock file in git as well.

```
poetry install
poetry run pip freeze > requirements.txt
```

## Run

```
poetry run flask run --reload
```

Or activate the environment first

```
poetry shell
flask run --reload
```
