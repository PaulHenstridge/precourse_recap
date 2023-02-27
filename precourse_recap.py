days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday"]

today = input("What day is it?")

daysLeft = len(days) - days.index(today)

print("only ", daysLeft, " days left to the weekend!!")
