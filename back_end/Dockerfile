FROM python:3.13.7-alpine
COPY --from=ghcr.io/astral-sh/uv:python3.13-alpine /uv /uvx /bin/

COPY . /webservice

WORKDIR /webservice
ENV PATH="/webservice/.venv/bin:$PATH"
RUN uv sync --locked

CMD [ "uv", "run", "--", "fastapi", "dev", "./src/main.py" ]
