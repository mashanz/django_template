# Django App Template

## Tech Stack

- Django
- Granian (Rust Python Server)
- DaisyUI (Tailwind CSS Components)
- Docker (Containerization)
- HTMX (Async content using AJAX)

## Requirements

- Python +3 (already installed on mac or ubuntu)
- Poetry +1.7 (`brew install poetry` or `sudo apt install poetry`)
- Make +3.81 (`brew install make` or `sudo apt install make`)
- Bun +1 (`brew tap oven-sh/bun && brew install bun`)

> no need to install virtual environment or venv or conda or anything else. because `poetry` is virtual package manager with `.venv` environment. Similar to npm/pnpm/yanr as package manager and `node_modules` as virtual environment

## Runing on Local

```bash
# Copy .env.example to .env and modify it
cp .env.example .env
# install dependencies
make
# run migrations
make migrate
# render tailwind
make tailwind
# render tailwind with watch mode
make tailwind-watch
# collect static for production
make collecstatic
# run dev server with watch mode
make dev
# run prod server
make prod
# run tests
make test
```
