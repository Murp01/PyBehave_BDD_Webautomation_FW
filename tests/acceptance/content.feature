Feature: Test that pages have the correct content
  These tests ensure the content on the page is displayed how expected

  Scenario: Blog page has a correct title
    Given I am on the blog page
    Then there is a title shown on the page
    And the title tag has content "This is the blog page"

  Scenario: Homepage has a correct title
    Given I am on the homepage
    Then there is a title shown on the page
    And the title tag has content "This is the homepage"

  Scenario: Blog page loads the posts
    Given I am on the blog page
    And I wait for the posts to load
    Then I can see there is a posts section on the page