# faulty calculator

print("\n\tPYTHON FAULTY CALCULATOR")
print("Read the instructions: ")
instructions =" 1 is for Addition,\n 2 is for Subtraction,\n 3 is for Multiplication,\n 4 is for Division."
print(instructions)

options = int(input("Choose a option: "))

def checkoptions(x):
    if options == 1 or options == 2 or options == 3 or options == 4:

        firstNumber = int(input("First number: "))
        secondNumber = int(input("Second number: "))

        def faultyCalculation(x , y):
            if firstNumber == 45 and secondNumber == 3:
              print("Multiplication of %d and %d is 555"% (firstNumber, secondNumber))

            elif firstNumber == 56 and secondNumber == 9:
              print("Addition of %d and %d is 77"% (firstNumber, secondNumber))

            elif firstNumber == 56 and secondNumber == 6:
              print("Division of %d and %d is 4"% (firstNumber , secondNumber))
            else:
                def calculations(x, y):
                    if options == 1:
                        print(f"Addition of {firstNumber} and {secondNumber} is {firstNumber + secondNumber}")

                    elif options == 2:
                        print(f"Subtraction of {firstNumber} and {secondNumber} is {firstNumber - secondNumber}")

                    elif options == 3:
                        print(f"Multiplication of {firstNumber} and {secondNumber} is {firstNumber * secondNumber}")

                    else:
                        print(f"Division of {firstNumber} and {secondNumber} is {firstNumber / secondNumber}")

                calculations(firstNumber, secondNumber)

        faultyCalculation(firstNumber, secondNumber)
    else:
        print("Invalid Option.")
checkoptions(options)
