Feature: Test that pages have the correct content
  These tests ensure the content on the page is displayed how expected

  Scenario: Blog page has the correct title
    Given I am on the blog page
    Then there is a title shown on the page
    And the title tag has content "This is the blog page"