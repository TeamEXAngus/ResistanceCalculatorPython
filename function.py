"""     ---Resistance Calculator Function---
This file contains a function that will determine the resistance of a resistor given its colour bands and returns this value as a string. This file also contains a dictionary with each valid colour and each possible value it could correspond to. The function takes a tuple or list with a length of at least three as its argument.
"""

#Dictionary containing each possible colour on a resistor and each value it could represent depending on position
#It's outputside of the function so that if neccesary it can be accessed through 'import'
colourValues = {
		    "black"   : [0    , 1           , None      , " 250ppm/K" ],
		    "brown"   : [1    , 10          , "±1%"     , " 100ppm/K" ],
		    "red"     : [2    , 100         , "±2%"     , " 50ppm/K"  ],
		    "orange"  : [3    , 1000        , None      , " 15ppm/K"  ],
		    "yellow"  : [4    , 10000       , None      , " 25ppm/K"  ],
		    "green"   : [5    , 100000      , "±0.5%"   , " 20ppm/K"  ],
		    "blue"    : [6    , 1000000     , "±0.25%"  , " 10ppm/K"  ],
		    "purple"  : [7    , 10000000    , "±0.1%"   , " 5ppm/K"   ],
		    "gray"    : [8    , 100000000   , "±0.05%"  , " 1ppm/K"   ],
        "white"   : [9    , 1000000000  , None      , None        ],
		    "gold"    : [None , 0.1         , "±5%"     , None        ],
		    "silver"  : [None , 0.01        , "±10%"    , None        ]
		} #Reference: https://eepower.com/uploads/education/resistor_color_codes_chart.png

#Function that takes a list of colours that could be found on a resistor and returns what resistance those colours in that order represents
def resistanceCalculate(colours):
  global colourValues
  
  #Raise an exceptions if arguments are invalid
  if type(colours) not in [type(()), type([])]:
    raise Exception("Argument must be a list or tuple!")

  if len(colours) < 3 or len(colours) > 6:
    raise Exception("Argument should be at least 3 colours and no more than 6 colours!")

  for colour in colours:
    if not colour in colourValues:
      raise Exception("Invalid colour selected!")

  #Inside try-block since this is the simplest way to validate the positions of colours in the function argument (More info at corresponding except-block)
  try:
    
    output = 0

    #Loop through the code for adding digits the appropriate number of times
    # 3 bands = 2 digits and 4 // 2 = 2 
    # 4 bands = 2 digits and 5 // 2 = 2
    # 5 bands = 3 digits and 6 // 2 = 3
    # 6 bands = 3 digits and 7 // 2 = 3
    for i in range ( ( len(colours) + 1 ) // 2 ):

      #Multiplies 'output' by ten so that each time the for-loop is run, a new digit is added rather than just adding two numbers together
      output *= 10
      output += colourValues[colours[i]][0]
  
    #Multiply 'output' by the correct multiplier for the colour
    output *= colourValues[colours[i+1]][1]

    #Sets 'tolerance' to the value corresponding to the correct colour band (band 4 on 4-band resistors or band 5 on 5-and-6-band resistors) or the default value for 3-band resistors
    if len(colours) == 4:
      tolerance = colourValues[colours[3]][2]
    elif len(colours) > 4:
      tolerance = colourValues[colours[4]][2]
    else: tolerance = "±20%"

    #Sets 'temp' to the value for the final band if the resistor has 6 bands
    temp = colourValues[colours[5]][3] if (len(colours) == 6) else ""

    #Returns a string containing the resistance value, the resistor's tolerance/precision, and the resistor's temperature coefficient
    return (str(output) + 'Ω' + tolerance + temp)

  #If the code in the try-block raises an exception, it will be because one or multiple elements in the 'colours' argument was in a position it should not be. This is because it has already been validated that the 'colours' argument is a valid data type, is at least a size of 3, and contains only valid colours so any errors must only be cause by attempting to access parts of a sub-array in 'colourValues' that do not exist.
  except:
    raise Exception("One or multiple of the given colours were in an invalid position.") 