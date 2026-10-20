# KeyGuardian Swarm - Autonomous Secret Leak Remediation

A swarm of 3 AI agents built with GPT-6 Astra on OmniRush that auto-detects and fixes exposed API keys.

## Problem
Developers leak keys like xpl_, sk-, AKIA, ghp_ causing security breaches.

## Agents
1. Scanner Agent (scanner.py): Scans codebase
2. Fixer Agent (fixer.py): Fixes to .env
3. Rebuilder Agent: Makes Dockerfile + requirements

## Setup
Python 3.11.0 is required (the version is pinned in `.python-version` and
`.runtime-version`). Install the locked dependencies with:

```sh
python -m pip install -r requirements.lock
```

cp .env.example .env

## Run
python scanner.py

## Test
make test

This is a Python project, so `npm test` is not applicable; use the repository
test command above.

## Docker
docker build -t keyguardian-swarm .
docker run keyguardian-swarm

## Rebuild checklist

- [x] Runtime pinned to Python 3.11.0
- [x] Application dependencies pinned in `requirements.lock`
- [x] Docker base image pinned to Python 3.11.0 slim
- [x] Dockerfile installs only the locked dependencies
- [x] Environment template is tracked and secrets are ignored
- [x] Rebuild uses the repository-local `make test` command
- [x] Test command runs without network access after dependencies are installed
- [x] Docker build and test verification recorded in `VERIFICATION.md`

## Built With
- OmniRush
- GPT-6 Astra (swarm mode)
- Python 3.11
