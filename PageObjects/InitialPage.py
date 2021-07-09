from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait as Wait
from selenium.webdriver.support import expected_conditions as ec

from PageObjects.Utility import Utility


class InitialPage(Utility):
    __language_selector_css = "div#language"
    __language_dropdown_list_css = "div[ng-bind-html='language']"
    __language_value_selected_css = "div#language span.ng-binding.ng-scope"
    __input_name_css = "input[name='name']"
    __input_org_name_css = "input[name='orgName']"
    __input_email_css = "input[type='email'][name='email']"
    __checkbox_agree_css = "input[type='checkbox'][ng-model='signUp.agree']+span"
    __button_submit_form_css = "button[type='submit']"
    __alert_element_css = "div.alert span"
    __text_header_css = "h2"
    __text_sub_header_css = "center.ng-binding"
    __text_terms_and_conditions_css = "label.ui-checkbox"
    __text_existing_account_css = "p.ng-binding"

    def __init__(self, driver):
        super().__init__(driver)

    def select_language(self, language):
        self.driver.find_element_by_css_selector(self.__language_selector_css).click()
        ddl = self.driver.find_elements_by_css_selector(self.__language_dropdown_list_css)
        for i in ddl:
            if i.text == language:
                i.click()
                return

    def verify_language_selected(self, language):
        assert self.driver.find_element_by_css_selector(self.__language_value_selected_css).text == language

    def fill_name(self, full_name):
        self.input_field_using_css_selector(full_name, self.__input_name_css)

    def fill_org_name(self, org_name):
        self.input_field_using_css_selector(org_name, self.__input_org_name_css)

    def fill_email(self, email):
        self.input_field_using_css_selector(email, self.__input_email_css)

    def accept_terms_n_conditions(self):
        self.driver.find_element_by_css_selector(self.__checkbox_agree_css).click()

    def submit_page(self):
        self.driver.find_element_by_css_selector(self.__button_submit_form_css).click()

    def verify_alert_for_sent_email(self):
        expected_text = "A welcome email has been sent. Please check your email."
        alert = Wait(self.driver, 1000, poll_frequency=1).until(
            ec.visibility_of_element_located((By.CSS_SELECTOR, self.__alert_element_css))
        )
        assert alert.text == expected_text

    def verify_name_placeholder(self, expected):
        actual = self.get_value_of_placeholder_with_css(self.__input_name_css)
        assert actual == expected, f"Expected: {expected} Actual:{actual}"

    def verify_org_name_placeholder(self, expected):
        actual = self.get_value_of_placeholder_with_css(self.__input_org_name_css)
        assert actual == expected, f"Expected: {expected} Actual:{actual}"

    def verify_email_placeholder(self, expected):
        actual = self.get_value_of_placeholder_with_css(self.__input_email_css)
        assert actual == expected, f"Expected: {expected} Actual:{actual}"

    def verify_header(self, expected):
        actual = self.driver.find_element_by_css_selector(self.__text_header_css).text
        assert actual == expected, f"Expected: {expected} Actual:{actual}"

    def verify_sub_header(self, expected):
        actual = self.driver.find_element_by_css_selector(self.__text_sub_header_css).text
        assert actual == expected, f"Expected: {expected} Actual:{actual}"

    def verify_tnc_text(self, expected):
        actual = self.driver.find_element_by_css_selector(self.__text_terms_and_conditions_css).text
        assert actual == expected, f"Expected: {expected} Actual:{actual}"

    def verify_submit_button_text(self, expected):
        actual = self.driver.find_element_by_css_selector(self.__button_submit_form_css).text
        assert actual == expected, f"Expected: {expected} Actual:{actual}"

    def verify_existing_account_text(self, expected):
        actual = self.driver.find_element_by_css_selector(self.__text_existing_account_css).text
        assert actual == expected, f"Expected: {expected} Actual:{actual}"
