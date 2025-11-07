FROM python:3.13.7-alpine
COPY --from=ghcr.io/astral-sh/uv:python3.13-alpine /uv /uvx /bin/

COPY . /web

WORKDIR /web
ENV PATH="/web/.venv/bin:$PATH"
RUN uv sync --locked

CMD [ "uv", "run", "--", "streamlit", "run", "./src/main.py" ]
