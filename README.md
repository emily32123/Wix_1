# Wix Domains — QA Assignment

**Total time spent:** To be updated after completing the assignment.

## Project Overview

This repository contains a QA assessment of Wix Domains.

The project explores the domain discovery experience across Wix's public interfaces and the public Domain Search API.

The main user question is: **Can I get this name?**

## Scope

The assessment covers:

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

Activate it on Windows PowerShell:

```powershell
.venv\Scripts\Activate.ps1
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Install the Playwright Chromium browser:

```bash
python -m playwright install chromium
```

### Environment Configuration

Create a local `.env` file in the project root.

Add the following variables:

```env
WIX_API_KEY=your_api_key_here
WIX_ACCOUNT_ID=your_account_id_here
```

Use your own Wix credentials. Do not commit `.env` or expose API keys.

The `.env.example` file contains placeholders only.

## Running Tests

Run all automated tests with one command:

```bash
python -m pytest -v
```

### Automated Test Coverage

The current test suite includes:

1. **API test:** Sends a request to the Wix Domain Search API and validates the HTTP status, response structure, domain name, and availability data type.
2. **UI smoke test:** Opens the Wix Domains storefront using Playwright and verifies that the page loads successfully and contains domain-related content.

The tests are designed to avoid purchasing or registering domains.

## Quality Strategy

1. Prioritize critical domain discovery user journeys.
2. Validate API contracts, response structures, and error handling.
3. Compare UI behavior with API responses when the information is equivalent.
4. Use stable assertions and avoid hardcoded dynamic suggestions or availability results.
5. Protect credentials, avoid destructive actions, and report only evidence-backed defects.

## One-Week Improvement Plan

1. **Day 1:** Expand API validation, including invalid inputs and error responses.
2. **Day 2:** Add more UI tests for domain search and input validation.
3. **Day 3:** Add coverage for supported and unsupported TLDs.
4. **Day 4:** Improve localization, pricing, and premium-domain test coverage.
5. **Day 5:** Add accessibility checks and improve test reporting.
6. **Day 6:** Configure CI execution and review test stability.
7. **Day 7:** Review findings, remove flaky tests, and improve documentation.

## Limitations

- Domain availability and suggestions may change over time.
- Pricing and results may depend on visitor location.
- The current automated suite provides smoke-level coverage, not exhaustive regression coverage.
- No purchases, registrations, load tests, or brute-force tests are performed.