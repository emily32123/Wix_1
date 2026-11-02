# Wix Domains — QA Assignment

**Total time spent:** Approximately 1 hour 20 minutes, from the first commit to final submission.

## Project Overview

This repository contains a QA assessment of Wix Domains.

The project explores the domain discovery experience across Wix's public interfaces and the public Domain Search API.

The main user question is: **Can I get this name?**

## Scope

- Wix Domains storefront
- Wix Business Name Generator
- Wix WHOIS lookup
- Public Domain Search API

## Repository Structure

- `ARCHITECTURE.md` — Observed architecture and network interactions.
- `TEST_PLAN.md` — QA scope, test scenarios, priorities, and approach.
- `FINDINGS.md` — Confirmed bugs, risks, and observations.
- `tests/` — Automated API and UI tests.
- `AI_LOG.md` — Documentation of AI assistance and human review.
- `.env.example` — Example environment variable configuration.
- `requirements.txt` — Python dependencies.

## Setup

### Prerequisites

- Python 3.10+
- Git
- A Wix account-level API key with the required Domain Search permissions.
- Wix Account ID.

### Installation

Create a virtual environment:

```bash
python -m venv .venv
```

Activate on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install Playwright Chromium:

```bash
python -m playwright install chromium
```

### Environment Configuration

Create `.env` in the project root:

```env
WIX_API_KEY=your_api_key_here
WIX_ACCOUNT_ID=your_account_id_here
```

Use your own Wix credentials. Do not commit `.env` or expose API keys.

`.env.example` contains placeholders only.

## Running Tests

Run all tests with one command:

```bash
python -m pytest -v
```

### Automated Coverage

1. **API test:** Checks domain availability through the Wix API, validates the HTTP status, response structure, domain, and availability field.
2. **UI smoke test:** Uses Playwright to open Wix Domains and verify that the page loads successfully and contains domain-related content.

Latest observed run: **2 passed**.

No purchases or registrations are performed.

## Quality Strategy

1. Prioritize critical domain discovery user journeys.
2. Validate API contracts, response structures, and error handling.
3. Compare UI behavior with API responses when equivalent.
4. Use stable assertions and avoid hardcoded dynamic suggestions or availability results.
5. Protect credentials, avoid destructive actions, and report only evidence-backed defects.

## One-Week Improvement Plan

- **Day 1:** Expand API tests for invalid inputs and error responses.
- **Day 2:** Add UI validation and search interaction tests.
- **Day 3:** Test supported and unsupported TLDs.
- **Day 4:** Investigate localization, pricing, and premium domain behavior.
- **Day 5:** Add accessibility checks and improve test reporting.
- **Day 6:** Add CI integration and improve test stability.
- **Day 7:** Review findings, coverage, and documentation.

## Limitations

- Domain availability and suggestions are dynamic.
- Prices and displayed options may depend on visitor location.
- Current automation is smoke-level and not exhaustive.
- No purchase, registration, load testing, or brute-force activity was performed.