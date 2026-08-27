# DevOps CI/CD 101

Learning DevOps through hands-on CI/CD pipeline building.

## Features

- Flask REST API with health checks
- Unit tests with pytest (6 tests)
- Code quality checks with flake8
- GitHub Actions automation
- Docker containerization
- Kubernetes deployment

## Setup

\\\ash
pip install -r requirements.txt
pytest tests/
flake8 app.py tests/
python app.py
\\\

## Test

\\\ash
pytest tests/ -v --cov=.
\\\

## Endpoints

- \GET /\ - Home endpoint
- \GET /health\ - Health check
- \GET /api/info\ - App info

## Status

Tests: ✅ Passing
