from behave import *

from selenium import webdriver

from page_models.pages.HomePage import HomePage
from page_models.pages.HudlPage import HudlPage
from page_models.pages.LoginPage import LoginPage

use_step_matcher('re')


@given('I am on the login page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    context.options = webdriver.ChromeOptions()
    context.options.add_argument("user-data-dir=C:\\temp\\")
    context.driver = webdriver.Chrome(options=context.options)
    page = LoginPage(context.driver)
    context.driver.get(page.url)
    context.driver.maximize_window()


# @given('I am on the login page')
# def step_impl(context):
#     context.driver = webdriver.Chrome()
#     page = LoginPage(context.driver)
#     context.driver.get(page.url)
#     context.driver.maximize_window()


@given('I am on the home page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = HomePage(context.driver)
    context.driver.get(page.url)
    context.driver.maximize_window()


@given('I am on Hudl main page')
def step_impl(context):
    context.driver = webdriver.Chrome()
    page = HudlPage(context.driver)
    context.driver.get(page.url)
    context.driver.maximize_window()


@then('I am on the home page')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the login page')
def step_impl(context):
    expected_url = LoginPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am redirected to the login page')
def step_impl(context):
    expected_title = 'Log In'
    assert context.driver.title == expected_title


@then('I am on Hudl main page')
def step_impl(context):
    expected_url = 'https://www.hudl.com/'
    assert context.driver.current_url == expected_url

