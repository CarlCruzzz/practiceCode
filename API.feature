Feature: API Testing
  Scenario: Get single user
    Given I send a Get request to "https://regres.in/api/users/2" with api key
    Then the response code should be 200