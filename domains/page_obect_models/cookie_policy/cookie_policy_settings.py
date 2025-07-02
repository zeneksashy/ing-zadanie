from playwright.sync_api import Page, Locator


class CookiePolicySettingsDialog:
    def __init__(self, page: Page):
        self.page = page
        self.dialog: Locator = page.locator('div.js-cookie-policy-settings').get_by_role("dialog")
        self.exit_button: Locator = self.dialog.locator('button.js-cookie-policy-settings-cancel-button')
        self.technical_toggle: Locator = self.dialog.locator('div[name="CpmTechnicalOption"]')
        self.analytical_toggle: Locator = self.dialog.locator('div[name="CpmAnalyticalOption"]')
        self.marketing_toggle: Locator = self.dialog.locator('div[name="CpmMarketingOption"]')
        self.decline_all_button: Locator = self.dialog.locator('button.js-cookie-policy-settings-decline-all-button')
        self.accept_selected_button: Locator = self.dialog.locator('button.js-cookie-policy-settings-decline-button')

    def exit(self):
        self.exit_button.click()

    def toggle_analytical(self):
        self.analytical_toggle.click()

    def toggle_marketing(self):
        self.marketing_toggle.click()

    def decline_all(self):
        self.decline_all_button.click()

    def accept_selected(self):
        self.accept_selected_button.click()
