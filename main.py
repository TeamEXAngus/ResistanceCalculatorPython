"""     ---Resistance Calculator---
This program takes a list of colours that could be found on the bands on a resistor and then determines what the value and precision of this resistor is. This program contains a function in 'function.py' to calculate the resistance, and input validation.
"""

import function #Imports the 'resistanceCalculate()' function from 'function.py'
from termcolor import colored #For printing coloured text

#List of valid colours
validColours = ["black", "brown", "red", "orange", "yellow", "green", "blue", "purple", "gray", "white", "silver", "gold"]

#Main program loop
done = False
while not done:

  #Get user input, either a command or a list of colours
  userInput = input(colored("Please input a list of colours separated only by commas,\nor 'help' for a list of valid colours, or 'exit' to exit.\n", "green"))

  if (userInput.lower()).replace(" ", "") == "help":
    print (colored(f"Valid colours are:\n{validColours}\n", "cyan"))
    continue

  elif (userInput.lower()).replace(" ", "") == "exit":
    done = True
    continue

  userInput = ((userInput.lower()).replace(" ", "")).split(",")

  #Inside try-except block for data validation
  try:
    #Print the value of a resistor with the given coloured bands
    print(colored(function.resistanceCalculate(userInput)+'\n', "yellow"))
    
  #Since 'resistanceCalculate()' has built-in data validation, a try-except block is all that's necessary to validate data
  except Exception as exception:
    #If the data is invalid, tell the user why
    print (colored(f"There was an error: {exception}\n", "red"))