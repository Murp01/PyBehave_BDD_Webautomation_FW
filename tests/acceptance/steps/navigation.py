from behave import *
from selenium import webdriver
import chromedriver_binary

use_step_matcher('re')

@given('I am on the homepage')
def step_impl(context):
    browser = webdriver.Chrome(executable_path=r"C:\Users\pmurp\PycharmProjects\video_code\tests\acceptance\steps\chromedriver.exe");
    #browser = webdriver.Chrome('chromedriver.exe')
    #browser.get('http:127.0.0.1:5000')
    browser.get('https://www.google.com')