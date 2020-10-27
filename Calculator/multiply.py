###
def multiplySetup():
    while True:
      try:
        global amount
        amount = int(input("How many numbers do you want to multiply?\n"))
        if amount > 1 and amount == int(amount):
            break
      except:
        print("\033[0;31mError: {} is not an acceptable arguement. Please enter an integer.".format(amount))
        continue
    multiplyStorage()

###
def multiplyStorage():
    x = 1
    y = "1"
    product = 1
    z = ""
    while x <= amount:
        user = input("Enter Number " + y + ":\n")
        z = z + " * " +user
        user = float(user)
        product = product * user
        x = x + 1
        y = int(y)
        y = y + 1
        y = str(y)
    product = str(product)
    print("The product is: " + product)
    z = z + " = " + product
    z = (z[3:len(z)])
    multiplyHistroy(z)
    print(z)

###
def multiplyHistroy(problem):
    mulHistory = open("history.txt", "a")
    mulHistory.write(problem + "\n")
    from choice import choose
    choose()

###
multiplySetup()

