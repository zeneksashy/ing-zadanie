from domains.page_obect_models.cookie_policy.cookie_policy_popup import CookiePolicyDialog
from domains.page_obect_models.cookie_policy.cookie_policy_settings import CookiePolicySettingsDialog


class MainPage:
    def __init__(self,page):
        self.page = page
        # cookies popup can be probably on every page
        self.cookie_policy_popup = CookiePolicyDialog(page)
        self.cookie_policy_settings = CookiePolicySettingsDialog(page)