import time
import sys
def choose():
    chooseInput = input("Press:\n1 --- Exit the calculator\n2 --- Enter another math problem\n3 --- Check the history\n")
    chooseInput = int(chooseInput)
    if chooseInput == 1:
        print("See you later!")
        print("Application closing in 3 seconds")
        time.sleep(1)
        print("Application closing in 2 seconds")
        time.sleep(1)
        print("Application closing in 1 second")
        time.sleep(1)
        sys.exit()
    elif chooseInput ==2:
        from problem import new
        new()
    elif chooseInput == 3:
        from hist import hist
        hist()