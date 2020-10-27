###
def new():
    print("\033[0;31m What function does your problem require?")
    print(
        " Type one of these symbols:\n *  ---  Multiplication\n /  ---  Division\n +  ---  Addition\n -  ---  Subtraction\n h --- History\n n --- New Math Problem")
    functionType = input()

    # Specific Opetator Excecution
    if ("*" in functionType or "multiplication" in functionType or "multiply" in functionType or "Multiplication" in functionType or "Multiply" in functionType or "MULTIPLICATION" in functionType or "MULTIPLY" in functionType):
        print("\033[0;34mMultiplication")
        from multiply import multiplySetup

    elif ("/" in functionType or "division" in functionType or "divide" in functionType or "Division" in functionType or "Divide" in functionType or "DIVISION" in functionType or "DIVIDE" in functionType):
        print("\033[0;35mDivision")
        from divide import divideSetup

    elif ("+" in functionType or "addition" in functionType or "add" in functionType or "Addition" in functionType or "Add" in functionType or "ADDITION" in functionType or "ADD" in functionType):
        print("\033[0;32mAddition")
        from add import addSetup

    elif ("-" in functionType or "subtraction" in functionType or "subtract" in functionType or "Subtraction" in functionType or "Subtract" in functionType or "SUBTRACTION" in functionType or "SUBTRACT" in functionType):
        print("\033[0;33mSubtraction")
        from subtract import subtractSetup

    elif ("h" in functionType or "history" in functionType or "History" in functionType or "HISTORY" in functionType):
        from hist import hist
        hist()

    elif ("n" in functionType or "New" in functionType or "new" in functionType or "NEW" in functionType or "New Math Problem" in functionType or "new math problem" in functionType or "NEW MATH PROBLEM" in functionType):
        from problem import new
        new()


