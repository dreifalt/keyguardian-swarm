# KeyGuardian Swarm - Autonomous Secret Leak Remediation

A swarm of 3 AI agents built with GPT-6 Astra on OmniRush that auto-detects and fixes exposed API keys.

## Problem
Developers leak keys like xpl_, sk-, AKIA, ghp_ causing security breaches.

## Agents
1. Scanner Agent (scanner.py): Scans codebase
2. Fixer Agent (fixer.py): Fixes to .env
3. Rebuilder Agent: Makes Dockerfile + requirements

## Setup
pip install -r requirements.txt
cp .env.example .env

## Run
python scanner.py

## Test
python test_scan.py

## Docker
docker build -t keyguardian-swarm .
docker run keyguardian-swarm

## Built With
- OmniRush
- GPT-6 Astra (swarm mode)
- Python 3.11
