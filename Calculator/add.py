###
def addSetup():
    while True:
      try:
        global amount
        amount = int(input("How many numbers do you want to add?\n"))
        if amount > 1 and amount == int(amount):
            break
      except:
        print("\033[0;31mError: {} is not an acceptable arguement. Please enter an integer.".format(amount))
        continue
    addStorage()

###
def addStorage():
    x = 1
    y = "1"
    sum = 0
    z = ""
    while x <= amount:
        user = input("Enter Number " + y + ":\n")
        z = z + " + " + user
        user = float(user)
        sum = sum + user
        x = x + 1
        y = int(y)
        y = y + 1
        y = str(y)
    sum = str(sum)
    print("The sum is: " + sum)
    z = z + " = " + sum
    z = (z[3:len(z)])
    addHistroy(z)
    print(z)

###
def addHistroy(problem):
    addHistory = open("history.txt", "a")
    addHistory.write(problem + "\n")
    from choice import choose
    choose()

###
addSetup()

