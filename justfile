set shell := ["powershell", "-NoLogo", "-NoProfile", "-Command"]

sync:
    uv sync

run:
    uv run reflex run

check:
    uv run ruff check .
    uv run pytest

format:
    uv run ruff format .
