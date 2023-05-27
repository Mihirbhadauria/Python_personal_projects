# This is my first project with little to no tutorials
# I am planning to make a CLI calculator then slow extend it to a GUI 
# I want to code in OOP format 

def user_input(lVal1, lVal2, lOperation):
     
    if lOperation == "+":
         result = lVal1 + lVal2
    
    elif lOperation == "*":
         result = lVal1 * lVal2
          
    elif lOperation == "-":
         result = lVal1 - lVal2       
     
    elif lOperation == "/":
         result = lVal1 - lVal2      

    print("\n" + str(result))
    return result

def main():
    print("Enter your first value")
    lVal1 = float(input())

    print("Enter your second value")
    lVal2 = float(input())

    print("Enter your desired opeartion simlar to normal calculator symbol")
    lOperation = input()

    user_input(lVal1, lVal2, lOperation)

if __name__ == "__main__":
    main()