from behave import *

from tests.acceptance.page_model.base_page import BasePage

use_step_matcher('re')

@then('there is a title shown on the page')
def step_impl(context):
    page = BasePage(context.driver)
    assert page.title.is_displayed()

@then('the title tag has content "(.*)"')
def step_impl(context, content):
    page = BasePage(context.driver)
    assert page.title_tag.text == content