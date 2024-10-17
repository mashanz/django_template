#!/bin/sh
GRANIAN_WORKERS=$(nproc --all) \
  uv run --no-dev granian \
  app.wsgi:application \
  --host 0.0.0.0 \
  --interface wsgi
