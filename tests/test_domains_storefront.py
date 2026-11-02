from playwright.sync_api import sync_playwright


def test_domains_storefront_loads():
    with sync_playwright() as playwright:
        browser = playwright.chromium.launch()
        page = browser.new_page()

        response = page.goto(
            "https://www.wix.com/domains",
            wait_until="domcontentloaded",
            timeout=60000,
        )

        assert response is not None
        assert response.status == 200

        page_text = page.locator("body").inner_text().lower()
        assert "domain" in page_text

        browser.close()