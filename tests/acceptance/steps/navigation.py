from behave import *
from selenium import webdriver
import chromedriver_binary

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\pmurp\PycharmProjects\video_code\tests\acceptance\steps\chromedriver.exe");
    #browser = webdriver.Chrome('chromedriver.exe')
    context.driver.get('http:127.0.0.1:5000')
    #context.browser.get('https://www.google.com')


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\pmurp\PycharmProjects\video_code\tests\acceptance\steps\chromedriver.exe");
    context.driver.get('http:127.0.0.1:5000/blog')


@then('I am on the blog page')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/blog'
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = 'http://127.0.0.1:5000/'
    assert context.driver.current_url == expected_url