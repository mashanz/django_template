# base
FROM python:3.12-slim-bookworm AS base
RUN python -m pip install poetry==1.6.1 --no-cache-dir
RUN apt update -y
RUN apt install curl -y
RUN apt install unzip -y
RUN curl -fsSL https://bun.sh/install | bash

FROM base AS dependency
WORKDIR /app
COPY . .
RUN poetry install --only main --no-root

# builder tw
FROM dependency AS builder_tw
WORKDIR /app
RUN ~/.bun/bin/bun install
RUN ~/.bun/bin/bunx tailwindcss -i ./app/base/static/base/css/base.css -o ./app/base/static/base/css/style.min.css --minify

FROM builder_tw AS builder_py
WORKDIR /app
COPY README.md README.md
RUN poetry build

# runner
FROM python:3.12-alpine AS runner
RUN addgroup -S nonroot \
  && adduser -S nonroot -G nonroot
WORKDIR /app
COPY --from=builder_py /app/dist/*whl .
RUN chown -R nonroot /app/*whl
USER nonroot
RUN pip install /app/*.whl --no-cache-dir --prefer-binary
USER root
RUN pip cache purge && rm /app/*whl
USER nonroot
WORKDIR /home/nonroot/.local/lib/python3.12/site-packages/app
EXPOSE 8000
ENV DEBUG=False
RUN python manage.py collectstatic
CMD ["python", "-m", "granian", "--host", "0.0.0.0", "--interface", "asgi", "app.asgi:application"]
