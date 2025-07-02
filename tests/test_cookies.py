import pytest
from playwright.sync_api import expect

from domains.page_obect_models.main_page import MainPage


@pytest.fixture
def main_page(page):
    page.goto("https://www.ing.pl/")
    return MainPage(page)


def test_analytics_cookies(main_page):
    expect(main_page.cookie_policy_popup.dialog).to_be_visible()
    initial_cookies = main_page.page.context.cookies()
    main_page.cookie_policy_popup.open_cookie_settings()
    main_page.cookie_policy_settings.toggle_analytical()
    main_page.cookie_policy_settings.accept_selected()
    cookies_afterwards = main_page.page.context.cookies()
    # requirements not clear, so let's just assume names are enough
    expected_values = {"cookiePolicyGDPR", "cookiePolicyGDPR__details", "cookiePolicyINCPS"}
    result = {cookie["name"] for cookie in cookies_afterwards} - {cookie["name"] for cookie in initial_cookies}
    assert expected_values == result
