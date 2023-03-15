Feature: Logout from Hudl website

  Scenario: Logout from Hudl website
    Given I am on the login page
    And I type in my valid email and password
    And I click on the login button
    And I am successfully logged in
    When I click on the logout button
    Then I am on Hudl main page