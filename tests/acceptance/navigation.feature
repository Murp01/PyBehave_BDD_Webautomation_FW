Feature: Test navigation between pages
  Description for the feature which can
  span over a few lines

  Scenario: Home page can go to blog
    Given I am on the homepage
    When I click on the "Go to blog" link
    Then I am on the blog page


  Scenario: Blog can go to homepage
    Given I am on the blog page
    When I click on the "Go to home" link
    Then I am on the homepage
