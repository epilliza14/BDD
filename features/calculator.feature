Feature: Calculator

  Scenario: Add two numbers
    Given I have a calculator
    When I add 2 and 3
    Then the result should be 5

  Scenario: Subtract two numbers
    Given I have a calculator
    When I subtract 5 from 8
    Then the result should be 3

  Scenario: Multiply two numbers
    Given I have a calculator
    When I multiply 4 by 6
    Then the result should be 24

  Scenario: Divide two numbers
    Given I have a calculator
    When I divide 10 by 2
    Then the result should be 5

  Scenario: Divide by zero
    Given I have a calculator
    When I divide 10 by 0
    Then I should receive an error saying "Cannot divide by zero"
