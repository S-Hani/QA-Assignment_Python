@signup
Feature: To check the signup functionality

  Scenario: To check if welcome mail is sent
    Given user is on signup page
    When user selects the language as "English"
    And user verifies the language as "English"
    And user submits the remaining details
    Then welcome email alert should be shown to the user
