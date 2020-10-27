###
def subtractSetup():
    while True:
      try:
        global amount
        amount = int(input("How many numbers do you want to subtract?\n"))
        if amount > 1 and amount == int(amount):
            break
      except:
        print("\033[0;31mError: {} is not an acceptable arguement. Please enter an integer.".format(amount))
        continue
    subtractStorage()

###
def subtractStorage():
    x = 1
    y = "1"
    difference = 0
    z = ""
    while x <= amount:
        if x == 1:
            put = input("Enter The Start Number: \n")
            difference = float(put)
        else:
            put = input("Enter Number " + y + ":\n")
            difference = difference - float(put)
        z = z + " - " + put
        difference = float(difference)
        x = x + 1
        y = int(y)
        y = y + 1
        y = str(y)
    difference = str(difference)
    print("The difference is: " + difference)
    z = z + " = " + difference
    z = (z[3:len(z)])
    subtractHistroy(z)
    print(z)

###
def subtractHistroy(problem):
    subtractHistory = open("history.txt", "a")
    subtractHistory.write(problem + "\n")
    from choice import choose
    choose()

###
subtractSetup()

