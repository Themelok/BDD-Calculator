Feature: Implementation of division feature

Scenario: Division of two positive numbers 
    Given two positive numbers
    When we divide first numbers by the second
    Then the result should be equal to quotient

Scenario: Division of two negative numbers 
    Given two negative numbers
    When we divide first numbers by the second
    Then the result should be equal to quotient

Scenario: Division of one positive and one negative number
    Given one positive number and one negative number.
    When we divide first numbers by the second
    Then the result should be equal to quotient

Scenario: Division of zero by any number
    Given zero as the first and one any number as the second
    When we divide first numbers by the second
    Then the result should be equal to zero

# Negative case: Division by zero
Scenario: Division of any number by zero
    Given any number as the first and  zero as the second
    When we divide first numbers by zero
    Then the result should be Error