# Hudl Login Exercise

## Overview
The goal of this exercise is to automate tests for a Login Page. Only some main Business flows were automated, meaning:
* Navigation From Hudl Main Page to Log In Page
* Log In With Valid Data
* Log In With Remember Me Option
* Log In With Invalid Data
* Logout
* Clear Cookies After Log In

These tests were chosen assuming they would be listed as Acceptance Criteria on the ticket. 
Second assumption is that all other data tests should have been performed on lower levels due to the cost of implementing system tests (email format, special characters, missing data, ...), the developers should have written all the unit and integration tests. And as a third assumption, there are contract tests in place as well.

Points to consider:
* Password reset cannot be fully automated, and would be faster to perform it manually than automating only half of the process.
* Usability, performance and security tests were not performed during this exercise, but would need to be considered before PROD deployment.
* Exploratory testing should still be performed before PROD deployment, e.g. login/logout while accessing the system through different tabs.

## Next Technical Steps
* Perform cross-browser testing.
* Use try/catch blocks when searching for an element.
* Put this project into a CI/CD pipeline.
* Refactor to avoid duplicated code.
* Change some asserts to find a specific element on screen in order to confirm current page.

## Getting Started
This project requires the use of Selenium Webdriver, Python 3.\*, Behave and Gherkin.

### IDE
As recommended IDE, download PyCharm Professional edition: https://www.jetbrains.com/pycharm/

After installing you can set-up a trial account.

Note: Professional edition is needed in order to have the links between the steps and the feature files (https://www.jetbrains.com/help/pycharm/creating-step-definition.html).

### Python
On the Terminal, execute the following command:

```python --version```

If there are no results, go to: https://www.python.org/downloads/ and download the latest Python version. Install Python 3.\*, and add Python to your system's PATH.

Keep in mind that, if using MacOS, replace `python` with `python3` in all commands needed to run the tests.

### Selenium
After installing Python, run the following command on the Terminal to install Selenium:

```python -m pip install selenium```

Download chromedriver (https://chromedriver.chromium.org/downloads), and add it to the system's PATH.

### Behave
From command line:

```python -m install behave```

## Running the Tests
The tests can be run from PyCharm. For that, navigate to `./tests/features` folder, where all the features are located. 
Open a feature, and click on the `>>` right beside the Scenario name to run all tests, or on the `>>` right beside the test 
to run only a specific case.

In order to run the tests from command line, open the Terminal, `cd` to the project folder:

```cd <hudl-login project path>```

Then, inside the project folder, execute the following command:

```behave ./tests/features/```

To execute a single feature:

```behave ./tests/features/<feature name>.feature```

## Issues
Password for test account is currently exposed with minimal encryption. Ideally, there would be a 1Password vault, for example, with the secrets.
