# Static Assets
FROM python:3.12-slim AS deps
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
RUN uv sync --no-cache --no-python-downloads  --frozen --no-dev

# collect static python
FROM deps AS build
COPY app /app
RUN uv run manage.py collectstatic --noinput

# Run Static
FROM ghcr.io/mashanz/cdn:0.1.3-static AS runner
WORKDIR /static
COPY --from=build /static /static
EXPOSE 8080
ENTRYPOINT [ "cdn" ]
