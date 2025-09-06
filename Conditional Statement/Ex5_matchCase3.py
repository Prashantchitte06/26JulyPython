num=6

match num:
    case 1:
        print("One")
    case 2 | 3:
        print("Two or Three")
    case 4 | 5:
        print("Four or Five")
    case 6:
        print("Six")
    case _:
        print("wrong input")
