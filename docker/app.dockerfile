FROM docker.io/python:3.12-slim AS deps
COPY --from=ghcr.io/astral-sh/uv:latest /uv /bin/uv
WORKDIR /app
COPY pyproject.toml pyproject.toml
COPY uv.lock uv.lock
COPY entrypoint.sh entrypoint.sh
RUN uv sync --no-cache --no-python-downloads --frozen --no-dev
FROM deps AS runner
COPY app /app
WORKDIR /app
EXPOSE 8000
ENTRYPOINT [ "./entrypoint.sh" ]
