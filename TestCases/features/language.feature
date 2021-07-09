@lang
Feature: To check the change language functionality

  Scenario: To check if language change is affected throughout the website
    Given user is on signup page
    When user selects the language as "Dutch"
    Then all the text on the screen should be in "Dutch"

  Scenario: To check default language for all fields is English
    Given user is on signup page
    # As English should be the Default language, we'll just verify it
    When user verifies the language as "English"
    Then all the text on the screen should be in "English"

