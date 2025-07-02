from playwright.sync_api import Locator, Page


class CookiePolicyDialog:
    def __init__(self, page: Page):
        self.page = page
        self.dialog: Locator = page.locator('div.js-cookie-policy-main').get_by_role("dialog")
        self.customize_button: Locator = self.dialog.locator('button.js-cookie-policy-main-settings-button')
        self.decline_button: Locator = self.dialog.locator('button.js-cookie-policy-main-decline-button')
        self.accept_button: Locator = self.dialog.locator('button.js-cookie-policy-main-accept-button')

    def accept_all(self):
        self.accept_button.click()

    def deny_all(self):
        self.decline_button.click()

    def open_cookie_settings(self):
        self.customize_button.click()