# Edge Lab

Edge computing laboratory and strategy engine.

## Project Structure

```
edge-lab/
├── src/edge_lab/          # Main package
│   ├── data/              # Data handling and processing
│   ├── engine/            # Core engine implementations
│   ├── strategies/        # Strategy implementations
│   └── api/               # API endpoints
├── tests/                 # Test suite
├── .github/workflows/     # GitHub Actions CI/CD
└── pyproject.toml         # Project configuration
```

## Development Setup

### Prerequisites

- Python 3.12+
- [uv](https://docs.astral.sh/uv/) - Fast Python package manager

### Installation

```bash
# Install dependencies
uv sync

# Install with dev dependencies
uv sync --all-extras
```

## Development Commands

### Linting

```bash
# Run ruff linter
uv run ruff check src tests

# Format code with ruff
uv run ruff format src tests
```

### Type Checking

```bash
# Run mypy type checker
uv run mypy src/edge_lab
```

### Testing

```bash
# Run all tests
uv run pytest

# Run with coverage report
uv run pytest --cov=src/edge_lab

# Run specific test file
uv run pytest tests/test_module.py -v
```

### Pre-commit Hooks

```bash
# Install git hooks
uv run pre-commit install

# Run hooks on all files
uv run pre-commit run --all-files
```

## CI/CD Pipeline

GitHub Actions automatically runs:
- **Lint**: Code style and import checks with ruff
- **Type Check**: Type safety with mypy
- **Test**: Unit tests with pytest, coverage reports on Python 3.12 and 3.13

See [.github/workflows/ci.yml](.github/workflows/ci.yml) for workflow configuration.

## License

MIT
