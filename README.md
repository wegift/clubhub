# clubhub

Custom integrations between GitLab and Clubhouse.

At WeGift we use Clubhouse for managing our work and GitLab for source control and code
review. This small app adds some functionality to make our lives easier.

At present this app:

- Adds "Code Review" and "QA" labels to Clubhouse cards when certain people approve
  approve a linked merge request in GitLab. 

## Install

I've used this project to try out [Poetry](https://python-poetry.org/) at WeGift. 
You'll need that first.

```
sudo apt-get install python3.8-venv
sudo pip install -U poetry
```

Then install project deps, poetry handles the virtualenv creation for you.

```
poetry install
```

## Dependency management

Heroku does not yet support Poetry, we need to maintain a lock file in git as well.

```
poetry install
poetry export -f requirements.txt --output requirements.txt
```

## Config

Copy the `.env.example` to `.env` and provide values. See `clubhub.settings` for a
description of each setting.

## Run

```
poetry run flask run --reload
```

Or activate the environment first

```
poetry shell
flask run --reload
```

## Deploy

At WeGift we deploy clubhub to Heroku. If internal talk to Will.
