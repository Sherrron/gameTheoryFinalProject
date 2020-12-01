# gameTheoryFinalProject
# This is the coding part for the project
There are two python files: classDef.py and main.py

classDef.py:
  We defines five types of players in this file, each with a class definition.
  In each class, the player has attributes 
    name (string), 
    strategies (dictionary), 
    payoff (integer),
    payoffrec (dictionary).
  Each player can call determineStrategy function to determine his strategy towards a specific player type, 
  and add the payoff by calling addPayoff function.
  
main.py:
  There is a play function, which represents a playing process between two players.
  By uncommenting the codes in the bottom and calling the main function, the results will be displayed.
