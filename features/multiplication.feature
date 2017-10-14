Feature: Implementation of multiplication feature

Scenario: Multiplication of two positive numbers 
    Given two positive numbers
    When we multiply first number by the second
    Then the result should be equal to product

Scenario: Multiplication of two negative numbers 
    Given two negative numbers
    When we multiply first number by the second
    Then the result should be equal to product

Scenario: Multiplication of one positive and one negative number.
    Given one positive number and one negative number.
    When we multiply first number by the second
    Then the result should be equal to product
