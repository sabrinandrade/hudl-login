import base64

from behave import *
from selenium import webdriver
from selenium.webdriver import ActionChains
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait

from tests.test_data.LoginData import LoginData
from page_models.locators.HomePageLocators import HomePageLocators
from page_models.locators.LoginPageLocators import LoginPageLocators
from page_models.pages.HomePage import HomePage
from page_models.pages.HudlPage import HudlPage
from page_models.pages.LoginPage import LoginPage

use_step_matcher('re')


@given('I type in my valid email and password')
def step_impl(context):
    page = LoginPage(context.driver)
    page.email.send_keys(LoginData.EMAIL)
    page.password.send_keys(base64.b64decode(LoginData.PASSWORD).decode())


@given('I type in my invalid email and valid password')
def step_impl(context):
    page = LoginPage(context.driver)
    page.email.send_keys(LoginData.WRONG_EMAIL)
    page.password.send_keys(base64.b64decode(LoginData.PASSWORD).decode())


@given('I type in my valid email and invalid password')
def step_impl(context):
    page = LoginPage(context.driver)
    page.email.send_keys(LoginData.EMAIL)
    page.password.send_keys(LoginData.WRONG_PASSWORD)


@given('I type in my invalid email and invalid password')
def step_impl(context):
    page = LoginPage(context.driver)
    page.email.send_keys(LoginData.WRONG_EMAIL)
    page.password.send_keys(LoginData.WRONG_PASSWORD)


@given("I select the remember me checkbox")
def step_impl(context):
    page = LoginPage(context.driver)
    page.remember_me.click()


@given("I click on the login button")
def step_impl(context):
    page = LoginPage(context.driver)
    page.login_button.click()


@given('I am successfully logged in')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.DISPLAY_NAME)
    )


@when('I click on the login button')
def step_impl(context):
    page = LoginPage(context.driver)
    page.login_button.click()


@when('I click on the logout button')
def step_impl(context):
    page = HomePage(context.driver)
    actions = ActionChains(context.driver)
    actions.move_to_element(page.display_name).perform()
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.LOGOUT_BUTTON)
    )
    page.logout_button.click()


@when('I click on Login Hudl')
def step_impl(context):
    page = HudlPage(context.driver)
    page.login_button.click()
    page.hudl_login_button.click()


@when('I am successfully logged in')
def step_impl(context):
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.DISPLAY_NAME)
    )


@when('I close the browser')
def step_impl(context):
    context.driver.close()


@when('I reopen the browser')
def step_impl(context):
    page = HomePage(context.driver)
    context.driver = webdriver.Chrome(options=context.options)
    context.driver.get(page.url)


@when("I delete the cookies")
def step_impl(context):
    context.driver.delete_all_cookies()


@when("I refresh the page")
def step_impl(context):
    context.driver.refresh()


@then('I am successfully logged in')
def step_impl(context):
    page = HomePage(context.driver)
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(HomePageLocators.DISPLAY_NAME)
    )
    assert "Sabrina A" == page.display_name.text


@then('I see an error display')
def step_impl(context):
    page = LoginPage(context.driver)
    expected_url = LoginPage(context.driver).url
    WebDriverWait(context.driver, 5).until(
        expected_conditions.visibility_of_element_located(LoginPageLocators.ERROR_DISPLAY)
    )
    assert "We didn't recognize that email and/or password." in page.error_display.text
    assert expected_url == context.driver.current_url

