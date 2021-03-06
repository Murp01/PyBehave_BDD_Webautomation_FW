from behave import *
from selenium import webdriver
import chromedriver_binary

from tests.acceptance.page_model.blog_page import BlogPage
from tests.acceptance.page_model.home_page import HomePage

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\pmurp\PycharmProjects\video_code\tests\acceptance\steps\chromedriver.exe");
    #browser = webdriver.Chrome('chromedriver.exe')
    #context.driver.get('https://www.google.com')
    page = HomePage(context.driver)
    context.driver.get(page.url)


@given('I am on the blog page')
def step_impl(context):
    context.driver = webdriver.Chrome(executable_path=r"C:\Users\pmurp\PycharmProjects\video_code\tests\acceptance\steps\chromedriver.exe");
    page = BlogPage(context.driver)
    context.driver.get(page.url)


@then('I am on the blog page')
def step_impl(context):
    expected_url = BlogPage(context.driver).url
    assert context.driver.current_url == expected_url


@then('I am on the homepage')
def step_impl(context):
    expected_url = HomePage(context.driver).url
    assert context.driver.current_url == expected_url
