Feature: Implementation of addition feature

Scenario: Addition of two positive numbers 
    Given two positive numbers
    When we add first numbers to second
    Then the result should be equal to summ

Scenario: Addition of two negative numbers 
    Given two negative numbers
    When we add first numbers to second
    Then the result should be equal to summ

Scenario: Addition of one positive and one negative number.
    Given one positive number and one negative number.
    When we add first numbers to second
    Then the result should be equal to summ
