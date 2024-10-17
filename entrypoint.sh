#!/bin/sh
GRANIAN_WORKERS=$(nproc --all) \
  uv run granian \
  app.wsgi:application \
  --host 0.0.0.0 \
  --interface wsgi
