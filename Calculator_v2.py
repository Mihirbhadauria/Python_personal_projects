# I have successfully created a calculator in python but now my goal is to 
# simplify the code and allow the user to get their calculation in one sentence

# This is my first project with little to no tutorials
# I am planning to make a CLI calculator then slow extend it to a GUI 
# I want to code in OOP format 

import re

def user_input(data):

    #In Python, you can't split a string with an empty separator ('') using the split() method. 
    #The method requires a delimiter to know where to split the string
    lTransformation = list(data)
    lTransformation = [item for item in data if item.strip()]

    #BUG Identifed - list data type seperates each digit into a seperate element in the list
    # so any 2 digits or more equations will not work 

    lLHS = float(lTransformation[0])
    lOperator = lTransformation[1]
    lRHS = float(lTransformation[2])

    if lOperator == "+":
        result = lLHS + lRHS
    
    elif lOperator == "*":
         result = lLHS * lRHS
          
    elif lOperator == "-":
         result = lLHS - lRHS       
     
    elif lOperator == "/":
         result = lLHS - lRHS      

    print(result)
    return result

def main():
    print("Enter what you want to calculate i.e 5 + 5")

    data = input()

    user_input(data)

if __name__ == "__main__":
    main()