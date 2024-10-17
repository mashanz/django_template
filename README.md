# Django App Template

## Tech Stack

- Nix (Declarative build and deployment)
- Django (Python Fullstack Framework)
- Granian (Rust Python Server)
- DaisyUI (Tailwind CSS Components)
- Podman/Docker (Containerization Tools)
- HTMX (Async content using AJAX)

## Requirements

Yes, just use nix and nix will manage everything

- [Nix](https://zero-to-nix.com/)

install nix with this command
```sh
curl --proto '=https' --tlsv1.2 -sSf -L https://install.determinate.systems/nix | sh -s -- install
```

> no need to install virtual environment or venv or conda or python or nodejs or bun or anything else. Because nix manage all of it

## Runing on Local

```bash

# Copy .env.example to .env and modify it
cp .env.example .env

# activate nix shell
nix-shell -p uv bun podman

# install dependency
uv sync
bun i

# run migrations
uv run app/manage.py migrate

# render tailwind
bun tw:build

# render tailwind with watch mode
bun tw:watch

# collect static for production
uv run app/manage.py collectstatic --noinput

# run dev server with watch mode
uv run app/manage.py runserver | bun tw:watch

# run tests docs
uv run interrogate -vvv

# check format lint
uv run ruff check app

# format app
uv run ruff format app
uv run djhtml app
```

## Simulation of deployment

```sh
# (optional) if you don't have podman machine instance initiated and running (make sure already inside nix-shell)
podman machine init
podman machine start

# run compose (rebuild to make sure latest update deployed)
podman compose up --build
```
