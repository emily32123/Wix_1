
import os

import pytest
import requests
from dotenv import load_dotenv


load_dotenv()

API_URL = (
    "https://www.wixapis.com/"
    "domain-search/v2/check-domain-availability"
)


def test_check_registered_domain_availability():
    api_key = os.getenv("WIX_API_KEY")
    account_id = os.getenv("WIX_ACCOUNT_ID")

    if not api_key or not account_id:
        pytest.skip("Wix API credentials are not configured")

    headers = {
        "Authorization": api_key,
        "wix-account-id": account_id,
    }

    response = requests.get(
        API_URL,
        headers=headers,
        params={"domain": "emilyclinic.com"},
        timeout=20,
    )

    assert response.status_code == 200, (
        f"Unexpected HTTP status: {response.status_code}"
    )

    data = response.json()

    assert "availability" in data
    assert data["availability"]["domain"] == "emilyclinic.com"
    assert isinstance(data["availability"]["available"], bool)