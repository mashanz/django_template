# Static Assets
FROM docker.io/python:3.12-slim AS deps
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync --no-cache --no-python-downloads  --frozen --no-dev

# bun install deps
FROM docker.io/oven/bun:latest AS bun
WORKDIR /app
COPY package.json package.json
COPY bun.lockb bun.lockb
RUN bun i

# build tailwind
FROM bun AS static
WORKDIR /app
COPY . .
RUN bun tw:build

# collect static python
FROM deps AS build
COPY --from=static /app/app /app
RUN uv run --no-dev manage.py collectstatic --noinput

# Run Static
FROM ghcr.io/mashanz/cdn:0.1.4-static AS runner
WORKDIR /static
COPY --from=build /static /static
EXPOSE 8080
ENTRYPOINT [ "cdn" ]
