Feature: Test the navigation to Log In page
  Instead of doing the navigation every time the login function needs to be tested,
  this feature covers the flow from the Hudl main page until the Log In page.

  Scenario: Test the link between Hudl page and Log In page
    Given I am on Hudl main page
    When I click on Login Hudl
    Then I am redirected to the login page