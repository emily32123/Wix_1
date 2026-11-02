# Test Plan

## 1. Objective

Evaluate the quality, functionality, and consistency of Wix domain discovery experiences across the public website interfaces and the public Domain Search API.

The main user question is: **Can I get this name?**

The testing focuses on helping users understand domain availability, discover alternative names, and retrieve domain registration information.

## 2. Scope

### In Scope

- Domain availability search.
- Domain input validation.
- Supported and unsupported TLD handling.
- Premium domain indications and pricing, where displayed.
- Business name and domain suggestions.
- Suggestion response structure and pagination.
- WHOIS/RDAP registration information.
- Privacy redaction.
- Public Domain Search API authentication, response structure, and error handling.
- Consistency between user-facing interfaces and API responses, where comparable.

### Out of Scope

- Purchasing, registering, or transferring domains.
- Load and stress testing.
- Brute-force testing or high-volume requests.
- Testing private or internal Wix systems.
- Accessing other users' accounts or private data.
- Testing functionality that requires unauthorized access.

## 3. Test Approach

The investigation combines:

1. **Manual exploratory testing** – Explore the three public user-facing experiences and inspect browser Network activity.
2. **API contract testing** – Validate documented request and response behavior of the public Domain Search API.
3. **Browser-based UI automation** – Automate selected user journeys using Playwright.
4. **Negative testing** – Check invalid input, unsupported TLDs, and error responses.
5. **Cross-interface comparison** – Compare results only when the interfaces provide equivalent information.
6. **Evidence-based reporting** – Record actual results and supporting evidence. Do not report assumptions as defects.

## 4. Test Scenarios

| ID | Scenario | Expected Result | Priority |
|---|---|---|---|
| TC-01 | Search for a registered domain such as `emilyclinic.com` | The storefront indicates that the domain is unavailable. | High |
| TC-02 | Search using an invalid domain format | The interface handles invalid input clearly and does not return misleading availability information. | High |
| TC-03 | Search for a domain with a supported TLD | The interface returns an availability result or a clear explanation. | High |
| TC-04 | Search for a domain with an unsupported TLD | The interface handles the unsupported TLD clearly and does not imply that Wix can sell it. | High |
| TC-05 | Inspect a premium domain result, when available | Premium status and applicable pricing are clearly indicated. | Medium |
| TC-06 | Search for a registered domain in WHOIS | Registration information is displayed when available. | Medium |
| TC-07 | Inspect WHOIS/RDAP privacy-sensitive fields | Redacted fields are handled without exposing private information or breaking the page. | Medium |
| TC-08 | Validate the public API response structure | The response matches the documented schema and expected data types. | High |
| TC-09 | Send an invalid or incomplete API request | The API returns an appropriate error response without exposing sensitive information. | High |
| TC-10 | Compare equivalent domain availability results across interfaces | Results are consistent when the same domain, context, and time are used. Differences are investigated and documented. | High |
| TC-11 | Inspect Business Name Generator suggestions | Suggestions contain valid domain formats and the expected response fields. | Medium |
| TC-12 | Inspect suggestion pagination | Pagination metadata is present and handled correctly when additional results are available. | Medium |
| TC-13 | Inspect localized suggestions and pricing | The interface presents understandable results for the current visitor context. | Medium |

## 5. Prioritization

- **High:** Core availability functionality, input validation, API contract, and error handling.
- **Medium:** Suggestions, WHOIS privacy behavior, premium information, pagination, and localization.
- **Low:** Cosmetic details that do not affect core functionality or user understanding.

Testing prioritizes the main user journey and the most important failure conditions within the assignment time limit.

## 6. Test Data

The following inputs may be used during testing:

| Input | Purpose |
|

Input

Purpose

emilyclinic.com

Registered-domain and WHOIS investigation

emilique

Business Name Generator exploration

invalid_domain.com

Invalid domain format

A domain with a TLD confirmed as supported

Supported TLD behavior

A TLD confirmed as unsupported by Wix

Unsupported TLD behavior

Additional inputs will be selected based on observed application behavior.

Test data must not contain personal or confidential information.

No domain registration or purchase will be performed.

7. Risks and Limitations

Domain availability is time-sensitive and may change between requests.

Search suggestions may vary between requests.

Results and pricing may depend on visitor location and currency.

Registry availability does not necessarily mean Wix supports selling the TLD.

Premium pricing may differ from standard registration and renewal pricing.

WHOIS/RDAP information may be redacted for privacy reasons.

Public API behavior and documentation may change.

A single manual observation is not sufficient evidence of a general defect.

The assignment time limit restricts the amount of test data and scenarios that can be investigated.

8. Test Execution and Reporting

For each executed test, record:

Test case ID.

Preconditions and test data.

Steps to reproduce.

Expected result.

Actual result.

Pass, fail, or blocked status.

Evidence, such as a relevant response or screenshot.

Severity and priority, when a defect is confirmed.

Only reproducible, evidence-backed defects will be reported as findings.

Observations and potential risks will be clearly distinguished from confirmed defects.

9. Automation Scope

The automation will focus on a small, stable set of high-priority checks:

Public API response validation.

Required response fields and data types.

Basic API error handling, where supported by the documented API.

At least one browser-based user journey.

The tests will avoid purchasing flows, high-volume requests, and dependencies on changing suggestion values.

API credentials will be loaded from environment variables and will not be committed to the repository.

10. Omissions

Testing will be limited to the assignment time budget and publicly accessible functionality.

The following are not covered:

Full cross-browser compatibility.

Performance and load testing.

Exhaustive TLD coverage.

Exhaustive localization testing.

Payment and checkout flows.

Internal Wix services and implementation details.