Feature: SauceDemo Login Suite

    @smoke @regresion
    Scenario Outline: Validating multiple user profiles
        Given I navigate to "https://www.saucedemo.com/"
        When I enter "<useito>" as username
        And I enter "<password>" as password
        And I click the login button
        Then I should see the products page title "Products"

        Examples: User Accounts
        | userito                 | password      | 
        | standard_user           | secret_sauce  |
        | problem_user            | secret_sauce  |
        | performance_glitch_user | secret_sauce  |

    @negativo
    Scenario: Login with invalid password
        Given I navigate to "https://www.saucedemo.com/"
        When I enter "standard_user" as username
        And I enter "wrong_password" as password
        And I click the login button
        Then I should see an error message containing "Username and password do not match"