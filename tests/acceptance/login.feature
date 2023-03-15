Feature: Login to Hudl website

  Scenario: Login with valid credentials
    Given I am on the login page
    And I type in my valid email and password
    When I click on the login button
    Then I am successfully logged in
    And I am on the home page

  Scenario: Login with invalid email
    Given I am on the login page
    And I type in my invalid email and valid password
    When I click on the login button
    Then I am on the login page
    And I see an error display

  Scenario: Login with invalid password
    Given I am on the login page
    And I type in my valid email and invalid password
    When I click on the login button
    Then I am on the login page
    And I see an error display

  Scenario: Login with valid credentials and remember me option
    Given I am on the login page
    And I type in my valid email and password
    And I select the remember me checkbox
    And I click on the login button
    And I am successfully logged in
    When I close the browser
    And I reopen the browser
    Then I am successfully logged in

  Scenario: Deleting cookies after login
    Given I am on the login page
    And I type in my valid email and password
    And I click on the login button
    And I am successfully logged in
    When I delete the cookies
    And I refresh the page
    Then I am redirected to the login page