
# Wix Domains — QA Assignment

**Total time spent:** To be updated after completing the assignment.

## Project Overview

This repository contains a QA assessment of Wix Domains.

The project explores the domain search experience across Wix's public interfaces and Domain Search API.

## Scope

The assessment covers:

- Wix Domains storefront
- Wix Business Name Generator
- Wix WHOIS lookup
- Public Domain Search API

## Repository Structure

- `ARCHITECTURE.md` — System architecture and observed network interactions.
- `TEST_PLAN.md` — QA scope, test scenarios, priorities, and approach.
- `FINDINGS.md` — Bugs, risks, and observations.
- `tests/` — Automated API and UI tests.
- `AI_LOG.md` — Documentation of AI assistance and review.

## Setup

### Prerequisites

- Python 3.10+
- Git
- A Wix account-level API key with the required Domain Search permissions.

### Installation

```bash
python -m venv .venv
```

Activate the virtual environment on Windows:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Create a local `.env` file based on `.env.example` and add your API key.

**Never commit your `.env` file or expose your API key.**

### Running Tests

Test execution instructions will be added after the automation setup.

## Quality Strategy

The assessment focuses on reliable domain-search behavior, API contract validation, user-facing results, error handling, and consistency across Wix's domain discovery experiences.

Automated tests will prioritize stable assertions and avoid assumptions about real-time domain availability.

## One-Week Improvement Plan

A potential follow-up plan:

1. Expand API and UI test coverage.
2. Add negative and boundary test scenarios.
3. Improve browser and localization coverage.
4. Add CI execution and test reporting.
5. Review accessibility and regression risks.
