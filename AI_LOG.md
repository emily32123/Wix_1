# AI Usage Log

## AI Tools Used

- ChatGPT by OpenAI (GPT-6).

## Purpose of AI Assistance

ChatGPT was used as an assistant and learning tool throughout the QA assignment.

Main areas of assistance:
- Breaking down the assignment requirements into manageable tasks.
- Understanding the Wix Domains user journeys and testing scope.
- Learning how to inspect browser network requests using Chrome DevTools.
- Understanding HTTP status codes, JSON responses, and API behavior.
- Planning the repository structure and documentation.
- Drafting and reviewing the architecture document, test plan, findings, and README.
- Understanding Python, pytest, Playwright, Git, and environment variables.
- Developing initial API and UI smoke tests.

## Prompts and Interactions

Examples of prompt topics and requests:
- "Help me break down the Wix Domains QA assignment step by step."
- "Guide me through inspecting Fetch/XHR requests in Chrome DevTools."
- "Help me understand this API response and what can be concluded from it."
- "Help me document the observed architecture and network interactions."
- "Help me create a practical test plan for this assignment."
- "Explain this Python API test and how to run it."
- "Help me create a Playwright smoke test."
- "Help me prepare the README and document the findings."

The interaction was iterative. Instructions and documentation were adjusted based on actual observations and command outputs.

## AI Errors, Limitations, and Corrections

- An HTTP 404 response was observed during the storefront investigation. Its request purpose was not confirmed, so it was documented as an investigation item rather than automatically classified as a product defect.
- An empty broker-offers response was observed. It was not treated as proof of domain unavailability.
- The relationship between the three Wix user-facing experiences and the public Domain Search API could not be fully verified. The architecture documentation explicitly identifies this limitation.
- Dynamic domain suggestions and availability results were not treated as stable expected values.
- WHOIS/RDAP privacy redaction was recognized as expected privacy behavior, not reported as a defect.

These examples demonstrate why AI explanations were checked against actual browser observations, API responses, and test execution.

## Changes and Suggestions Not Accepted

- No unverified relationship between backend requests was presented as fact.
- No defect was reported solely because an HTTP request returned 404.
- No conclusion about domain availability was drawn from an unrelated or empty response.
- Dynamic suggestions were not hardcoded as expected test results.
- No purchase or registration flow was performed.

## Human Review and Validation

The following work was performed and checked manually:
- Inspected the three public Wix user journeys using Chrome DevTools.
- Reviewed actual request names, HTTP statuses, and response bodies.
- Created and configured the local project and environment variables.
- Ran the API test and reviewed its result.
- Ran the Playwright storefront smoke test and reviewed its result.
- Reviewed Git status and committed project changes.
- Checked that the actual `.env` file was excluded from Git.

All submitted code and documentation were reviewed during development. I am responsible for understanding and explaining the submitted work.

## Work Not Delegated to AI

- Creating and managing the Wix account-level API key.
- Inspecting the actual Wix application behavior and network responses.
- Running the tests and checking their results.
- Making final decisions about test coverage, priorities, and findings.
- Deciding whether an observation is a confirmed defect.
- Managing Git commits and the public repository.
- Final review and explanation of the submission.

## Agent Configuration

- No autonomous coding agent or project-specific agent configuration was used.
- ChatGPT provided explanations, suggestions, and draft content.
- Commands, code, and documentation were reviewed by the human before use.

## Reflection

AI helped accelerate learning, planning, and documentation. However, its suggestions were treated as hypotheses rather than evidence. Actual application behavior was checked manually, tests were executed, and conclusions were limited to what could be supported by observations.

The QA decisions and responsibility for the final submission remain with the human author.