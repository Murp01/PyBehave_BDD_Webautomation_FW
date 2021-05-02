Feature: Test navigation between pages
  Description for the feature which can
  span over a few lines

  Scenario: Home page can go to blog
    Given I am on the homepage
    When I click on the link with id "blog-link"
    Then I am on the blog page


  Scenario: Blog can go to homepage
    Given I am on the blog page
    When I click on the link with id "home-link"
    Then I am on the homepage
