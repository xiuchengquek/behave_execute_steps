Feature: Addition
    In order to avoid silly mistakes
    As a math dimwit
    I want to be told the sum of two numbers

Scenario: Run first scenario
   Given I have entered into the calculator:
   """
   50
   """
   And I entered a 2nd variable into the calculator:
   """
   100
   """
   When I press add
   Then the results should be 150 on the screen


Scenario: Add 50 to the results above
   Given the results above
   And I entered another variable into the calculator:
   """
   100
   """
   When I press add this time wround
   Then the results hould be 250
