from time import sleep

from Constants.constants import ENGLISH, DUTCH
from Constants.user_info import AUTHOR_NAME, AUTHOR_EMAIL_ID
from PageObjects.InitialPage import InitialPage
from pytest_bdd import scenarios, given, when, then, parsers


scenarios('../features')


class TestSolution:
    page = None

    @staticmethod
    def select_language(language):
        TestSolution.page.select_language(language)

    @staticmethod
    def verify_language(language):
        TestSolution.page.verify_language_selected(language)

    @staticmethod
    def enter_details_and_submit():
        TestSolution.page.fill_name(AUTHOR_NAME)
        TestSolution.page.fill_org_name(AUTHOR_NAME)
        TestSolution.page.fill_email(AUTHOR_EMAIL_ID)
        TestSolution.page.accept_terms_n_conditions()
        TestSolution.page.submit_page()

    @staticmethod
    def verify_alert_for_sent_email():
        TestSolution.page.verify_alert_for_sent_email()

    @staticmethod
    def verify_all_test_for_language(language):
        sleep(0)
        TestSolution.page.verify_language_selected(language)
        if language == ENGLISH["Language"]:
            TestSolution.page.verify_header(ENGLISH["Main-header"])
            TestSolution.page.verify_sub_header(ENGLISH["Sub-header"])
            TestSolution.page.verify_name_placeholder(ENGLISH["Name-field-placeholder"])
            TestSolution.page.verify_org_name_placeholder(ENGLISH["OrgName-field-placeholder"])
            TestSolution.page.verify_email_placeholder(ENGLISH["Email-field-placeholder"])
            TestSolution.page.verify_tnc_text(ENGLISH["TnC-text"])
            TestSolution.page.verify_submit_button_text(ENGLISH["Submit-button-text"])
            TestSolution.page.verify_existing_account_text(ENGLISH["account-text"])
        elif language == DUTCH["Language"]:
            TestSolution.page.verify_header(DUTCH["Main-header"])
            TestSolution.page.verify_sub_header(DUTCH["Sub-header"])
            TestSolution.page.verify_name_placeholder(DUTCH["Name-field-placeholder"])
            TestSolution.page.verify_org_name_placeholder(DUTCH["OrgName-field-placeholder"])
            TestSolution.page.verify_email_placeholder(DUTCH["Email-field-placeholder"])
            TestSolution.page.verify_tnc_text(DUTCH["TnC-text"])
            TestSolution.page.verify_submit_button_text(DUTCH["Submit-button-text"])
            TestSolution.page.verify_existing_account_text(DUTCH["account-text"])


@given('user is on signup page')
def user_is_on_signup_page(setup):
    TestSolution.page = InitialPage(setup)


@when(parsers.parse('user selects the language as "{language}"'))
def user_selects_the_language_as(language):
    TestSolution.select_language(language)


@when(parsers.parse('user verifies the language as "{language}"'))
def user_verifies_the_language_as(language):
    TestSolution.verify_language(language)


@when('user submits the remaining details')
def user_submits_the_remaining_details():
    TestSolution.enter_details_and_submit()


@then('welcome email alert should be shown to the user')
def welcome_email_alert_should_be_shown_to_the_user():
    TestSolution.verify_alert_for_sent_email()


@then(parsers.parse('all the text on the screen should be in "{language}"'))
def all_the_text_on_the_screen_should_be_in(language):
    TestSolution.verify_all_test_for_language(language)
