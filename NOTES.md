## How to build

in the package root directory do the following

```
uv sync --group dev
uv run pytest
uv build
```

then in the project that needs it

```
uv add /path/to/alps_py-*.whl
```
