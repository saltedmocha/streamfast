FROM python:3.13.7-alpine
COPY --from=ghcr.io/astral-sh/uv@sha256:8f26991a5b32c59ecd1800b5d7f212d2af4910979ea21c592ad88048dd494cfe /usr/local/bin/uv /usr/local/bin/uvx /usr/local/bin/

COPY . /web

WORKDIR /web
ENV PATH="/web/.venv/bin:$PATH"
RUN uv sync --locked

CMD [ "uv", "run", "--", "streamlit", "run", "./src/main.py" ]
