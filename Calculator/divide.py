###
def divideSetup():
    while True:
      try:
        global amount
        amount = int(input("How many numbers do you want to divide?\n"))
        if amount > 1 and amount == int(amount):
            break
      except:
        print("\033[0;31mError: {} is not an acceptable arguement. Please enter an integer.".format(amount))
        continue
    divideStorage()

###
def divideStorage():
    x = 1
    y = "1"
    quotient = 1
    z = ""
    while x <= amount:
        if x == 1:
            put = input("Enter The Start Number: \n")
            quotient = float(put)
        else:
            put = input("Enter Number " + y + ":\n")
            quotient = quotient / float(put)
        z = z + " / " + put
        quotient = float(quotient)
        x = x + 1
        y = int(y)
        y = y + 1
        y = str(y)
    quotient = str(quotient)
    print("The quotient is: " + quotient)
    z = z + " = " + quotient
    z = (z[3:len(z)])
    divideHistroy(z)
    print(z)

###
def divideHistroy(problem):
    divideHistory = open("history.txt", "a")
    divideHistory.write(problem + "\n")
    from choice import choose
    choose()

###
divideSetup()

