FROM debian:bullseye-slim AS base

RUN apt update && apt install -y --no-install-recommends \
    ca-certificates \
    curl \
    git \
    libgl1 \
    libegl1 \
    libopengl0
RUN curl -Ls "https://github.com/prefix-dev/pixi/releases/latest/download/pixi-$(uname -m)-unknown-linux-musl" \
    -o /usr/local/bin/pixi \
    && chmod +x /usr/local/bin/pixi


FROM base AS final

# first, copy only the requirements to cache the layer
COPY pixi.toml pixi.lock pyproject.toml /app/
RUN mkdir /app/src \
    && cd /app \
    && pixi install --locked -e prod -v \
    && pixi clean cache --yes


COPY config/config_prod.yaml /app/config/config.yaml
COPY src /app/src

WORKDIR /app

CMD ["pixi", "run", "-e", "prod", "main"]