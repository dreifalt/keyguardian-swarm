# Rebuild verification

The repository's rebuild checklist is complete (8/8):

- [x] Python 3.11.0 is pinned in `.python-version` and `.runtime-version`.
- [x] Dependencies are pinned in `requirements.lock`.
- [x] The Docker base image is pinned to `python:3.11.0-slim`.
- [x] Docker installs only the locked dependency file.
- [x] `.env.example` is tracked and `.env` is ignored.
- [x] `make test` is the single project test command.
- [x] The test command is local/offline once dependencies are installed.
- [x] Docker build and test results are recorded below.

## Latest run

- `make test`: **PASS**
- `docker build -t keyguardian-swarm .`: **NOT RUN** — Docker is not installed in
  the current verification environment. Run this command on a Docker-enabled
  Linux host to complete the container verification.
