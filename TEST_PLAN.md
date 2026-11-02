
# Test Plan

## 1. Objective

Evaluate the quality and consistency of Wix domain discovery experiences across the public website interfaces and Domain Search API.

## 2. Scope

### In Scope

- Domain availability search.
- Domain name validation.
- Supported and unsupported TLDs.
- Premium domain indications and pricing.
- Search suggestions.
- WHOIS information and privacy redaction.
- API response structure and error handling.
- Consistency between the different entry points.

### Out of Scope

- Purchasing or registering domains.
- Load and stress testing.
- Brute-force testing.
- Testing private or internal Wix systems.
- Testing outside the publicly available interfaces and authorized API access.

## 3. Test Approach

- Manual exploratory testing.
- API contract testing.
- Browser-based UI automation.
- Negative and boundary testing.
- Cross-interface comparison.

## 4. Test Scenarios

| ID | Scenario | Priority |
|---|---|---|
| TC-01 | Search for a valid domain name | High |
| TC-02 | Search for an invalid domain format | High |
| TC-03 | Search with a supported TLD | High |
| TC-04 | Search with an unsupported TLD | High |
| TC-05 | Identify premium domain results | Medium |
| TC-06 | Verify WHOIS privacy redaction | Medium |
| TC-07 | Validate API response structure | High |
| TC-08 | Verify API error handling | High |
| TC-09 | Compare results across entry points | High |
| TC-10 | Verify localized pricing and suggestions | Medium |

## 5. Prioritization

- High: Core functionality, API contract, and user-facing search behavior.
- Medium: Pricing, localization, privacy, and secondary functionality.
- Low: Visual details that do not affect core functionality.

## 6. Risks and Limitations

- Domain availability can change at any time.
- Search suggestions may vary between requests.
- Results and pricing may depend on visitor location.
- Wix may not support every TLD.
- WHOIS data may be redacted for privacy reasons.
- Public API behavior may be subject to change.

## 7. Test Data

Use safe, non-purchasing search inputs.

No domain registration or purchase will be performed.

## 8. Reporting

Document each finding with:

- Description
- Reproduction steps
- Expected result
- Actual result
- Evidence
- Severity
- Priority

## 9. Omissions

Testing will be limited to the assignment time budget and publicly accessible functionality.