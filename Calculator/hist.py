def hist():
    viewHistory = open("history.txt", "r")
    def openHistory():
        print(viewHistory.read())
        from choice import choose
        choose()
    openHistory()