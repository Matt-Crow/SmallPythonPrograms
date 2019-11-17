quitProgram = False

while not quitProgram:
    done = False
    #done with current calculations
    total = 0
    itemCount = 0

    while not done:
        item = input("enter a number, or 'q' to show calculations:")
        try:
            item = float(item)
            total += item
            itemCount += 1
        except Exception as error:
            print(error)
        if item == "q":
            done = True
    print("DATA:")
    print("TOTAL: " + str(total))
    print("COUNT: " + str(itemCount))
    print("AVG: " + str(total / itemCount))

    if input("Continue? y/n") == "n":
        quitProgram = True
