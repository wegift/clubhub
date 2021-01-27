<h1>
  <img src="https://gitlab.com/wegift/clubhub/-/raw/master/logo.png" height=32 float=left>
  clubhub
</h1>

Custom integrations between GitLab and Clubhouse.

At WeGift we use Clubhouse for managing our work and GitLab for source control and code
review. This small app adds some functionality to make our work easier.

| Event | GitLab | Clubhouse |
| ----- | ------ | --------- |
| On MR approval in GitLab adds "Code Review" and "QA" labels to linked Clubhouse card. | ![](https://gitlab.com/wegift/clubhub/-/raw/master/screenshots/mr-approve.png) | ![](https://gitlab.com/wegift/clubhub/-/raw/master/screenshots/clubhouse-code-review.png) |

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
