Feature: Implementation of subtraction feature

Scenario: Subtraction of two positive numbers 
    Given two positive numbers
    When we subtract second number from first number
    Then the result should be equal to difference

Scenario: Subtraction of two negative numbers 
    Given two negative numbers
    When we subtract second number from first number
    Then the result should be equal to difference

Scenario: Subtraction of one positive and one negative number.
    Given one positive number and one negative number.
    When we subtract second number from first number
    Then the result should be equal to difference