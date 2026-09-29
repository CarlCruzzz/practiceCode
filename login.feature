Feature: Login funcionality
    Scenario: Successful Login with valid credentials
        Given user is on the login page
        When user enters valid username and password
        And click on the login button
        Then user should be navigated to the product page
